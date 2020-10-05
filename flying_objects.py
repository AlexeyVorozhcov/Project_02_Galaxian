import pygame
from math import tan, pi, cos
import mydef
import random
import public_vars
from space_objects.bonuses import Bonus_crystall_small, Bonus_crystall_big

g=10
rad = 180/pi


class Flying_object(pygame.sprite.Sprite):
    image1 = mydef.load_image('Data/shots/01 - main - standart_gun.png')
    image2 = mydef.load_image('Data/shots/05 - vrag - standart_gun.png')
    image3 = mydef.load_image('Data/shots/08 - vrag - cosinus_gun.png')
    bonus_pack = [Bonus_crystall_small, Bonus_crystall_big]
    def __init__(self, x0, y0, tetta, v, speed ):
        super().__init__(public_vars.explosion_group)
        self.type = ''
        self.image = random.choice([self.image1, self.image2, self.image3,])
        self.rect = self.image.get_rect()
        self.x0 = x0
        self.x = self.x0
        self.y0 = y0
        self.y = self.y0
        self.tetta = tetta
        self.v = v
        self.tetta1 = self.tetta / rad
        self.rect.x = self.x
        self.rect.y = self.y
        # if self.rect.y > 600:
        #     self.kill()
        # self.time = pygame.time.get_ticks()
        self.speed = speed
        self.is_stop = False

    def update(self):
        if not self.is_stop:
            self.x += self.speed
            self.xx = self.x - self.x0
            # self.y = self.x * tan(self.tetta1) - 1 / (2 * self.v ** 2) * (g * self.x ** 2) / (cos(self.tetta1) ** 2) + self.y0
            self.y = self.xx * tan(self.tetta1) - ((self.xx**2)*(g/(2*self.v**2*cos(self.tetta1)**2)))
            self.rect.x = self.x
            self.rect.y = self.y0 - self.y
            self.time = pygame.time.get_ticks()
            print (self.x, self.y)
            if abs(self.xx)>40: self.is_stop = mydef.random_chance([False, True], [870, 130])
        else:
            random.choice(self.bonus_pack)(self.x, self.rect.y)
            self.kill()

class Flying_Bonus(pygame.sprite.Sprite):
    img=[]
    img.append(mydef.load_image('Data/bonus_fly.png'))
    img.append(mydef.load_image('Data/bonus_crystall_fly.png'))
    def __init__(self, type, x0, y0, x1, y1, speed = 100 ):
        super().__init__(public_vars.labelsprites_group)
        self.image = self.img[type]
        self.rect = self.image.get_rect()
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x = 0
        self.y = 0
        self.t = 0
        self.step = 1 / speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.is_stop = False

    def update(self):
        if not self.is_stop:
            self.t += self.step
            if self.t > 1: self.is_stop = True
            self.x = self.x0 + (self.x1-self.x0)*self.t
            self.y = self.y0 + (self.y1-self.y0)*self.t
            # print((self.t, self.x, self.y))
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.kill()


class Flying_star(Flying_Bonus):
    pass