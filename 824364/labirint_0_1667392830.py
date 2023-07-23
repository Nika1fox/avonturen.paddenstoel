from pygame import *

#клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
    
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    #метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#клас головного гравця
class Player(GameSprite):
    #метод, у якому реалізовано управління спрайтом за кнопками стрілочкам клавіатури
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    ''' переміщає персонажа, застосовуючи поточну горизонтальну та вертикальну швидкість'''
    def update(self):  
        # Спершу рух по горизонталі
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # йдемо праворуч, правий край персонажа - впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # якщо торкнулися відразу кількох, то правий край - мінімальний із можливих
        elif self.x_speed < 0: # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # якщо торкнулися кількох стін, то лівий край - максимальний
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # йдемо вниз
            for p in platforms_touched:
                # Перевіряємо, яка з платформ знизу найвища, вирівнюємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # йдемо вгору
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) # вирівнюємо верхній край по нижніх краях стінок, на які наїхали
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

#клас спрайту-ворога

class Enemy_q(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.x <= 1100: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 90:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy_w(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.x <= 220: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 350:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy_e(GameSprite):
    side = "up"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.y <= 200: #w1.wall_x + w1.wall_width
            self.side = "down"
        if self.rect.y >= win_height - 80:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy_r(GameSprite):
    side = "up"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.y <= 100: #w1.wall_x + w1.wall_width
            self.side = "down"
        if self.rect.y >= win_height - 180:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

# клас спрайту-кулі
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.x > win_width+10:
            self.kill()

#Створюємо віконце
win_width = 1350
win_height = 690
display.set_caption("Лабіринт")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load("jungle.png"), (win_width, win_height)) # задаємо колір відповідно до колірної схеми RGB

#Створюємо групу для стін
barriers = sprite.Group()

#створюємо групу для куль
bullets = sprite.Group()

#Створюємо групу для монстрів
monsters = sprite.Group()

#Створюємо стіни картинки
w1 = GameSprite('platform.png', 90, 190, 150, 15)
w2 = GameSprite('platform1.png', 90, 600, 15, 200)
w3 = GameSprite('platform.png', 225, 587, 150, 15)
w4 = GameSprite('platform1.png', 90, 400, 15, 200)
w5 = GameSprite('platform.png', 370, 587, 150, 15)
w6 = GameSprite('platform1.png',90, 100, 15, 200)
w7 = GameSprite('platform.png', 630, 587, 150, 15)
w8 = GameSprite('platform1.png',225, 0, 15, 200)
w9 = GameSprite('platform.png', 775, 587, 150, 15)
w10 = GameSprite('platform1.png', 225, 200, 15, 200)
w11 = GameSprite('platform.png', 370, 400, 150, 15)
w12 = GameSprite('platform1.png', 225, 400, 15, 200)
w13 = GameSprite('platform.png', 370, 90, 150, 15)
w14 = GameSprite('platform1.png', 505, 400, 15, 200)
w15 = GameSprite('platform.png', 660, 90, 150, 15)
w16 = GameSprite('platform1.png', 910, 400, 15, 200)
w17 = GameSprite('platform.png', 515, 285, 150, 15)
w18 = GameSprite('platform1.png', 910, 600, 15, 200)
w19 = GameSprite('platform.png', 660, 90, 150, 15)
w20 = GameSprite('platform1.png', 505, 95, 15, 200)
w21 = GameSprite('platform.png', 805, 90, 150, 15)
w22 = GameSprite('platform1.png', 650, 95, 15, 200)
w23 = GameSprite('platform.png', 950, 90, 150, 15)
w24 = GameSprite('platform1.png', 1085, 95, 15, 200)
w25 = GameSprite('platform.png', 950, 285, 150, 15)
w26 = GameSprite('platform1.png', 1085, 290, 15, 200)
w27 = GameSprite('platform.png', 1205, 90, 150, 15)
w28 = GameSprite('platform1.png', 1085, 490, 15, 200)
w29 = GameSprite('platform.png', 1205, 285, 150, 15)
w30 = GameSprite('platform1.png', 1205, 290, 15, 200)
w31 = GameSprite('platform.png', 660, 185, 150, 15)

#додаємо стіни до групи
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
barriers.add(w23)
barriers.add(w24)
barriers.add(w25)
barriers.add(w26)
barriers.add(w27)
barriers.add(w28)
barriers.add(w29)
barriers.add(w30)
barriers.add(w31)


#створюємо спрайти
packman = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)
monster1 = Enemy_q('anti-hero.png', win_width - 80, 200, 80, 80, 5)
monster2 = Enemy_w('anti-hero.png', win_width - 300, 305, 80, 80, 5)
monster3 = Enemy_e('anti-hero.png', win_width - 1220, 200, 80, 80, 5)
monster4 = Enemy_r('anti-hero.png', win_width - 530, 100, 80, 80, 5)
final_sprite = GameSprite('bonbon.png', win_width - 85, win_height - 100, 80, 80)

#додаємо монстра до групи
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)

#змінна, що відповідає за те, як закінчилася гра
finish = False

# музика
mixer.init()
mixer.music.load("music1.mp3")
mixer.music.play(-1)


# монети
font.init()
font1 = font.SysFont('arial', 25)

coins_amount_1 = 0

coin1 = GameSprite('coin.png', 160, 170, 20, 20)
coin2 = GameSprite('coin.png', 575, 265, 20, 20)
coin3 = GameSprite('coin.png', 1000, 665, 20, 20)
coin4 = GameSprite('coin.png', 450, 565, 20, 20)
coin5 = GameSprite('coin.png', 1270, 300, 20, 20)
coin6 = GameSprite('coin.png', 1015, 265, 20, 20)
coin7 = GameSprite('coin.png', 720, 165, 20, 20)
coins = sprite.Group()
coins.add(coin1)
coins.add(coin2)
coins.add(coin3)
coins.add(coin4)
coins.add(coin5)
coins.add(coin6)
coins.add(coin7)
#ігровий цикл
run = True
while run:
    #цикл спрацьовує кожну 0.05 секунд
    time.delay(50)
        #перебираємо всі події, які могли статися
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0 
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0

#перевірка, що гра ще не завершена
    if not finish:
        #оновлюємо фон кожну ітерацію
        window.blit(back, (0,0))#зафарбовуємо вікно кольором
        
        #запускаємо рухи спрайтів
        packman.update()
        bullets.update()
        monster1.update()
        monster2.update()
        monster3.update()
        monster4.update()

        #оновлюємо їх у новому місці при кожній ітерації циклу
        packman.reset()
        
        #рисуємо стіни 2
        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)

        coins.update()
        coins.draw(window)

        if sprite.spritecollide(packman, coins, True):
            coins_amount_1 += 1
        coin = font1.render(f'Монеток : {coins_amount_1}/7', True, (204, 255, 153))
        window.blit(coin, (545, 10))


        #Перевірка зіткнення героя з ворогом та стінами
        if sprite.spritecollide(packman, monsters, False):
            finish = True
            # обчислюємо ставлення
            img = image.load('lose.png')
            d = img.get_width() // img.get_height()
            window.blit(transform.scale(img, (win_height * d, win_height)), (0, 0))

        if sprite.collide_rect(packman, final_sprite) and coins_amount_1 == 7:
            finish = True
            img = image.load('thumb.png')
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
    display.update()