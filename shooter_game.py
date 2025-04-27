from pygame import *
from random import randint
mixer.init()
font.init()

number = 0
score2 = 0

bullets = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_wigth, sprite_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sprite_wigth, sprite_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        kp = key.get_pressed()
        if kp[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if kp[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if kp[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if kp[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet('pulka.png', self.rect.centerx - 11, self.rect.top - 15, 4, 25, 25)       
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global number
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(75, 625)
            self.rect.y = 0
            self.speed = randint(1, 2)
            number += 1

    def update2(self, n):
        if self.rect.y < 500:
            self.rect.y += self.speed
        if n >= 2000:
            self.rect.x = randint(75, 625)
            self.rect.y = 0
            self.speed = randint(1, 2)
            n = 0
        n += 1
        return n

class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 5:
            self.rect.y -= 10
        else:
            self.kill()


win = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
display.set_caption('Space_vision')

player = Player('rocket2.png', 350, 425, 7, 75, 75)

enemies = sprite.Group()
for i in range(3):
    ufo = Enemy('ufo.png', randint(75, 625), 0, randint(1, 2), 75, 75)
    enemies.add(ufo)

pump_up = Enemy('update.png',  randint(75, 625), 0, randint(1, 2), 50, 50)

font2 = font.Font(None, 35)
tip = font2.render('Нажми "R", чтобы начать заново', True, (255, 0, 0))
tip2 = font2.render('Нажми пробел, чтобы пропустить обучение', True, (0, 255, 255))

font1 = font.Font(None, 70)
winn = font1.render('YOU WIN!', True, (0, 255, 255))
lose = font1.render('YOU LOSE!', True, (255, 0, 0))

text = font1.render('В НАШУ ГАЛАКТИКУ', True, (0, 255, 255))
text15 = font1.render('ВТОРГЛИСЬ', True, (0, 255, 255))
text16 = font1.render('ИНОПЛАНЕТЯНЕ!', True, (0, 255, 255))

text2 = font1.render('С ЦЕЛЬЮ ЗАВОЕВАТЬ', True, (0, 255, 255))
text3 = font1.render('НАШУ ПЛАНЕТУ!', True, (0, 255, 255))

text4 = font1.render('ТВОЯ ЦЕЛЬ - ', True, (0, 255, 255))
text5 = font1.render('НЕДОПУСТИТЬ ЭТОГО!', True, (0, 255, 255))

text6 = font1.render('НА ЗЕМЛЮ НЕЛЬЗЯ', True, (0, 255, 255))
text7 = font1.render('ПРОПУСТИТЬ', True, (0, 255, 255))

text8 = font1.render('БОЛЕЕ ДВУХ', True, (0, 255, 255))
text9 = font1.render('ИНОПЛАНЕТЯН!', True, (0, 255, 255))

text10 = font1.render('ТАКЖЕ ТВОЙ КОРАБЛЬ', True, (0, 255, 255))

text11 = font1.render('НЕ ВЫДЕРЖИТ СТОЛКНОВЕНИЕ', True, (0, 255, 255))
text12 = font1.render('С ЛЮБЫМ ДРУГИМ ОБЪЕКТОМ!', True, (0, 255, 255))

text13 = font1.render('БУДЬ ОСТОРОЖЕН!', True, (0, 255, 255))

text14 = font1.render('УДАЧИ!', True, (0, 255, 255))


mixer.music.load('space2.ogg')
mixer.music.play()

laser = mixer.Sound('laser.ogg')
boom = mixer.Sound('boom.ogg')

clock = time.Clock()
FPS = 60
clock.tick(FPS)

game = True
finish = False

n = 1000
n2 = 0
n3 = 0
n4 = 20
flag = 0

a = 3000
b = 3000
c = 3000
d = 3000
e2 = 3000
f = 3000
g = 3000
h = 3000
i = 3000

training = 1

while game:

    kp = key.get_pressed()

    if training == 1:
        win.fill((0, 0, 0))

        if a > 0:
            win.blit(text, (30, 100))
            win.blit(text15, (30, 200))
            win.blit(text16, (30, 300))
            a -= 1
        elif b > 0:
            win.blit(text2, (30, 150))
            win.blit(text3, (30, 300))
            b -= 1
        elif c > 0:
            win.blit(text4, (30, 150))
            win.blit(text5, (30, 300))
            c -= 1
        elif d > 0:
            win.blit(text6, (30, 150))
            win.blit(text7, (30, 300))
            d -= 1
        elif e2 > 0:
            win.blit(text8, (30, 150))
            win.blit(text9, (30, 300))
            e2 -= 1
        elif f > 0:
            win.blit(text10, (30, 200))
            a -= 1
        elif g > 0:
            win.blit(text11, (30, 150))
            win.blit(text12, (30, 300))
            g -= 1
        elif h > 0:
            win.blit(text13, (30, 200))
            h -= 1
        elif i > 0:
            win.blit(text14, (30, 200))
            i -= 1
        win.blit(tip2, (100, 430))
        if kp[K_SPACE] or i <= 0:
            training = 2
            

    elif finish == False:

        win.blit(background, (0, 0))
        player.reset()
        player.update()
        enemies.draw(win)
        enemies.update()
        bullets.draw(win)
        bullets.update()
        pump_up.reset()
        n2 = pump_up.update2(n2)

        score = font2.render('Счёт: ' + str(score2), True, (255, 255, 255))
        lost = font2.render('Пропущено: ' + str(number), True, (255, 255, 255))
        
        if n >= n4:
            #if kp[K_SPACE]:
            laser.play()
            player.shoot()
            n = 0
        n += 1 

        collides = sprite.groupcollide(enemies, bullets, True, True)
        for c in collides:
            boom.play()
            score2 += 1
            ufo = Enemy('ufo.png', randint(75, 625), 0, randint(1, 3), 75, 75)
            enemies.add(ufo)

        if sprite.collide_rect(pump_up, player):
            flag = 1
        if flag == 1:
            if n3 < 1000:
                n4 = 0
                n3 += 1
            else:
                n4 = 20
                n3 = 0
                flag = 0



        # if sprite.spritecollide(player, enemies, False) or number >= 3:
        #     finish = True
        # if finish == True:
        #     win.blit(lose, (200, 200))
        #     win.blit(tip, (150, 250))       

        win.blit(score, (3, 3))
        win.blit(lost, (3, 23))

    if finish == True and kp[K_r]:
        player.rect.x = 350
        player.rect.y = 425
        score2 = 0
        number = 0
        enemies = sprite.Group()
        for i in range(5):
            ufo = Enemy('ufo.png', randint(75, 625), 0, randint(1, 3), 75, 75)
            enemies.add(ufo)
        finish = False

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()