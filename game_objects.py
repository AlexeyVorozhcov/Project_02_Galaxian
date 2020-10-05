import pygame
import random
import mydef
import sounds
from math import cos



TYPE = ['main_spaceship', 'spaceship', 'bomb', 'shot_main', 'shot_spaceship', 'bonus_shots', 'bonus_health', 'bonus_protect', 'protect_field', 'bonus']
NAMES = ['main_spaceship', 'simple_spaceship', 'fast_spaceship', 'superfast_ship', 'big_ship' ]

class Scale_of_XP(pygame.sprite.Sprite):
    def __init__(self, obj, color):
        super().__init__(obj.group)
        self.obj = obj
        self.color = color
        self.d = obj.rect.width - 1
        self.p = self.d / obj.max_health
        self.image = pygame.Surface((self.d, 5))
        pygame.draw.rect(self.image, color, (0, 0, self.d, 4), 1)
        pygame.draw.rect(self.image, color, (0, 0, int(self.p * obj.health), 4), 0)
        self.rect = self.image.get_rect()
        self.rect.x = obj.rect.x
        self.rect.y = obj.rect.y-5

    def update(self):
        if self.obj.health<=0:
            self.kill()
        self.p = self.d / self.obj.max_health
        self.image = pygame.Surface((self.d, 5))
        pygame.draw.rect(self.image, self.color, (0, 0, self.d, 4), 1)
        pygame.draw.rect(self.image, self.color, (0, 0, int(self.p * self.obj.health), 4), 0)
        self.rect.x = self.obj.rect.x
        self.rect.y = self.obj.rect.y-5

class Direction():
    D_RIGTH = [1, 0]
    D_DOWN = [0, 1]
    D_LEFT = [-1, 0]
    D_UP = [0, -1]
    D_STOP = [0, 0]
    D_RIGTH_DOWN = [1, 1]
    D_LEFT_DOWN = [-1, 1]
    D_RIGTH_UP = [1, -1]
    D_LEFT_UP = [-1, -1]

class Space_Object(pygame.sprite.Sprite):
    def __init__(self, gameboard, group):
        super().__init__(group)
        self.name = ""
        self.type = None
        self.num_step = 0
        self.gameboard = gameboard
        self.group = group
        self.is_shot = False
        # Свойства по умолчанию, устанавливаются наследниками
        self.general_direction = None
        self.direction = None
        self.speed = None
        self.gun = None
        self.health = None
        self.type_explosion = None
        self.value = 0


    # проверка выхода объекта за экран
    def check_out_screen(self):
        if self.type != "protect_field":
            out_up = self.rect.y < 0
            out_down = self.rect.bottom > self.gameboard.h
            if self.name == 'alien_ship':
                out_down = self.rect.bottom > self.gameboard.h+50
            if self.type == 'main_spaceship':
                out_left = self.rect.left < 0
                out_right = self.rect.right > self.gameboard.w
                if out_right or out_down or out_left or out_up:
                    self.rect = self.last_rect
            else:
                out_left = self.rect.right < 0 - 50
                out_right = self.rect.left > self.gameboard.w + 50
                if out_right or out_down or out_left or out_up:
                    self.kill()


    # движение
    def to_move(self):
        # делаем шаг
        self.last_rect = self.rect
        self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * self.speed)
        self.num_step += 1
        # проверяем выход за границы
        self.check_out_screen()

    # выстрел
    def to_shot(self):
        if self.gun.is_shot and self.gun.shots > 0:
            if self.general_direction==Direction.D_RIGTH:
                x = self.rect.right + 1
            else:
                x = self.rect.left - 1
            if mydef.check_timer(self.gun.periodcity_time, self.gun.periodicity):
                Shot(self.gun, self.gameboard, self.group, x, y=self.rect.centery)
                # self.gun(self.gameboard, self.group, x, y=self.rect.centery)
                self.gun.periodcity_time = pygame.time.get_ticks()
                self.gun.shots -= 1


    def to_destruction(self, uron=1):
        return_points = 0
        self.health -= uron
        if self.health <=0:
            return_points = self.value
            if self.name!='big_ship' and self.type!='shot_main' and self.type!='bonus_shots' and self.type!='bonus_health' and self.type!='bonus':
                sounds.play_sound(2)
            else:
                if self.type!='shot_main' and self.type!='bonus_shots' and self.type!='bonus_health' and self.type!='bonus':
                    sounds.play_sound(3)
                elif self.type=='bonus_shots' and self.type=='bonus_health':
                    sounds.play_sound(4)
                elif self.type =='bonus':
                    sounds.play_sound(5)

            Explosion(self, is_kill=True)
            if self.type == 'spaceship':
                if random.randint(0, 10)>7:
                    random.choice([Bonus_health, Bonus_shot, Bonus_protect]) (self.gameboard, self.group, x=self.rect.centerx, y=self.rect.centery)
            self.kill()
        else:
            #sounds.play_sound(1)
            Explosion(self, is_kill=False)
        return return_points

    def update(self):
        self.to_move()
        if self.gun != None:
            self.to_shot()

class Main_ship(Space_Object):
    image = mydef.load_image('Data/main_spaceship.png')
    mask = pygame.mask.from_surface(image)
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'main_spaceship'
        self.type = 'main_spaceship'
        self.image = Main_ship.image
        self.rect = self.image.get_rect()
        self.mask = Main_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 5
        self.general_direction = Direction.D_RIGTH
        self.direction = Direction.D_STOP
        # self.gun = gun.Standart_gun_main_01
        self.gun = Gun_main_ship() #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 10
        self.health = self.max_health
        self.value = 0 # сколько очков этот объект даст при уничтожении
        self.points = 0
        self.uron = 2
        self.protect = None
        self.scale_of_XP = Scale_of_XP(self, (102,255,0) )
        self.is_help_shots = False


class Protect_field(Space_Object):
    image = mydef.load_image('Data/pole.png')
    mask = pygame.mask.from_surface(image)
    def __init__(self, ship, gameboard, group):
        super().__init__(gameboard, group)
        self.ship = ship
        self.name = 'protect_field'
        self.type = 'protect_field'
        self.image = Protect_field.image
        self.rect = self.image.get_rect()
        self.mask = Protect_field.mask
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery
        self.last_rect = self.rect
        self.speed = ship.speed
        self.general_direction = ship.general_direction
        self.direction = Direction.D_STOP
        self.gun = None  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 0  # сколько очков этот объект даст при уничтожении
        self.uron = 1
        #self.p = (255 // self.max_health) * self.health


    def update(self):
        super().update()
        self.rect.centerx = self.ship.rect.centerx
        self.rect.centery = self.ship.rect.centery
        #self.p = (255//self.max_health)*self.health
        #self.image.set_alpha(self.p)

class Simple_ship(Space_Object):
    image = mydef.load_image('Data/spaceship_01.png')
    mask = pygame.mask.from_surface(image)
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'simple_spaceship'
        self.type = 'spaceship'
        self.image = Simple_ship.image
        self.rect = self.image.get_rect()
        self.mask = Simple_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = Gun_simple_ship() #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 1 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 2
        self.health = self.max_health
        self.value = 10 # сколько очков этот объект даст при уничтожении
        self.uron = 1

    def update(self):
        super().update()
        if (self.num_step % 50 == 0):
            self.gun.is_shot = True
        if (self.num_step % 60 == 0):
            self.gun.is_shot = False

class Fast_ship(Space_Object):
    image = mydef.load_image('Data/spaceship_02.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'fast_spaceship'
        self.type = 'spaceship'
        self.image = Fast_ship.image
        self.rect = self.image.get_rect()
        self.mask = Fast_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 4
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = Gun_simple_ship()  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 1  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 3
        self.health = self.max_health
        self.value = 30  # сколько очков этот объект даст при уничтожении
        self.uron = 2

    def update(self):
        super().update()
        if (self.num_step % 50 == 0):
            self.gun.is_shot = True
        if (self.num_step % 60 == 0):
            self.gun.is_shot = False

class Superfast_ship(Space_Object):
    image = mydef.load_image('Data/kosmolet_06.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'superfast_ship'
        self.type = 'spaceship'
        self.image = Superfast_ship.image
        self.rect = self.image.get_rect()
        self.mask = Superfast_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 5
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = Gun_superfast_ship()  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 4
        self.health = self.max_health
        self.value = 50  # сколько очков этот объект даст при уничтожении
        self.uron = 3

    def update(self):
        super().update()
        if (self.num_step % 50 == 0):
            self.gun.is_shot = True
        if (self.num_step % 60 == 0):
            self.gun.is_shot = False

class Big_ship(Space_Object):
    image_template = mydef.load_image('Data/kosmolet_07.png')
    mask = pygame.mask.from_surface(image_template)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'big_ship'
        self.type = 'spaceship'
        self.image = Big_ship.image_template
        self.rect = self.image.get_rect()
        self.mask = Big_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 1
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = Gun_big_ship()  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 4  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 50
        self.health = self.max_health
        self.value = 250  # сколько очков этот объект даст при уничтожении
        self.uron = 5
        self.scale_of_XP = Scale_of_XP(self,(255,36,0))

    def update(self):
        super().update()
        if (self.num_step % 50 == 0):
            self.gun.is_shot = True
        if (self.num_step % 60 == 0):
            self.gun.is_shot = False

class Alien_ship(Space_Object):
    image = mydef.load_image('Data/kosmolet_08.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'alien_ship'
        self.type = 'spaceship'
        self.image = Alien_ship.image
        self.rect = self.image.get_rect()
        self.mask = Alien_ship.mask
        #self.rect.x = x
        #self.rect.y = y
        #self.last_rect = self.rect
        self.speed = 7
        self.general_direction = Direction.D_LEFT
        self.direction = random.choice([Direction.D_LEFT_UP, Direction.D_LEFT_DOWN])
        if self.direction == Direction.D_LEFT_UP:
            self.rect.x = random.randint (gameboard.w - 200, gameboard.w)
            self.rect.y = gameboard.h-1
        else:
            self.rect.x = random.randint(gameboard.w - 200, gameboard.w)
            self.rect.y = 1
        self.last_rect = self.rect
        self.gun = None  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 70  # сколько очков этот объект даст при уничтожении
        self.uron = 2

class Remove_ship(Space_Object):
    image = mydef.load_image('Data/kosmolet_09.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'remove_ship'
        self.type = 'spaceship'
        self.image = Remove_ship.image
        self.rect = self.image.get_rect()
        self.mask = Remove_ship.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 3
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = Gun_simple_ship()  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 1  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 3
        self.health = self.max_health
        self.value = 70  # сколько очков этот объект даст при уничтожении
        self.uron = 2

    def update(self):
        super().update()
        if (self.num_step % 50 == 0):
            self.gun.is_shot = True
        if (self.num_step % 60 == 0):
            self.gun.is_shot = False
        if (self.num_step % 40 == 0):
            self.direction = random.choice([Direction.D_LEFT_UP, Direction.D_LEFT_DOWN, Direction.D_LEFT])
        if (self.num_step % 70 == 0):
            self.direction = random.choice([Direction.D_LEFT_UP, Direction.D_LEFT_DOWN, Direction.D_LEFT])

class Meteorit(Space_Object):
    images = mydef.get_load_images('Data/meteorits', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'meteorit'
        self.type = 'bomb'
        self.image = random.choice(Meteorit.images)
        self.rect = self.image.get_rect()
        self.mask = Meteorit.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 3
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 3 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 10 # сколько очков этот объект даст при уничтожении
        self.uron = 1


class Heavy_Meteorit(Space_Object):
    images = mydef.get_load_images('Data/meteorits2', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'heavy_meteorit'
        self.type = 'bomb'
        self.image = random.choice(Heavy_Meteorit.images)
        self.rect = self.image.get_rect()
        self.mask = Heavy_Meteorit.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 3 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 3
        self.health = self.max_health
        self.value = 30 # сколько очков этот объект даст при уничтожении
        self.uron = 3

class Super_Meteorit(Space_Object):
    image = mydef.load_image('Data/super_meteorit.png')
    mask = pygame.mask.from_surface(image)
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'super_meteorit'
        self.type = 'bomb'
        self.image = Super_Meteorit.image
        self.rect = self.image.get_rect()
        self.mask = Super_Meteorit.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 1
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 4 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 120
        self.health = self.max_health
        self.value = 250 # сколько очков этот объект даст при уничтожении
        self.uron = 10
        self.scale_of_XP = Scale_of_XP(self, (255, 36, 0))

class Bonus_shot(Space_Object):
    image = mydef.load_image('Data/Ammunition_Icon.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'bonus_shots'
        self.type = 'bonus_shots'
        self.image = Bonus_shot.image
        self.rect = self.image.get_rect()
        self.mask = Bonus_shot.mask
        self.rect.x = x
        self.rect.y = y
        self.start_y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 0
        self.health = self.max_health
        self.value = 200  # сколько патронов содержит
        self.uron = 0



    def update(self):
        super().update()
        self.rect.y = 10 * cos(0.10 * self.num_step) + self.start_y


class Bonus_protect(Bonus_shot):
    image = mydef.load_image('Data/Armor_Icon.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group, x, y)
        self.name = 'bonus_protect'
        self.type = 'bonus_protect'
        self.image = Bonus_protect.image
        self.rect = self.image.get_rect()
        self.mask = Bonus_protect.mask
        self.rect.x = x
        self.rect.y = y
        self.start_y = y
        self.last_rect = self.rect
        self.value = 50  # сколько патронов содержит


class Bonus_health(Bonus_shot):
    image = mydef.load_image('Data/HP_Icon.png')
    mask = pygame.mask.from_surface(image)

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group, x, y)
        self.name = 'bonus_health'
        self.type = 'bonus_health'
        self.image = Bonus_health.image
        self.rect = self.image.get_rect()
        self.mask = Bonus_health.mask
        self.rect.x = x
        self.rect.y = y
        self.start_y = y
        self.last_rect = self.rect
        self.speed = 2
        self.value = 50  # сколько здоровья для передачи содержит


class Bomb(Space_Object):
    image = mydef.load_image('Data/bomb_01.png')
    mask = pygame.mask.from_surface(image)
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'bomb'
        self.type = 'bomb'
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.mask = Bomb.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 5 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 10 # сколько очков этот объект даст при уничтожении
        self.uron = 1

class Shot(Space_Object):
    def __init__(self, gun,gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = gun.name
        self.type = gun.type
        self.image = gun.image_shot
        self.mask = gun.mask
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = gun.speed
        self.general_direction = gun.general_direction
        self.direction = gun.direction
        self.type_explosion = 0 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 0 # сколько очков этот объект даст при уничтожении
        self.points = 0
        self.uron = gun.uron

    def to_shot(self):
        pass


class Gun_main_ship():
     name = 'standart_gun'
     type = 'shot_main'
     obj_shot = Shot
     image_shot =  mydef.load_image('Data/shots/01 - main - standart_gun.png')
     mask =  pygame.mask.from_surface(image_shot)
     speed = 12
     general_direction = Direction.D_RIGTH
     direction = Direction.D_RIGTH
     periodicity = 60
     uron = 1
     periodcity_time = pygame.time.get_ticks()
     shots = 500
     is_shot = False


class Gun_simple_ship():
    name = 'gun_main_ship'
    type = 'shot_spaceship'
    image_shot = mydef.load_image('Data/shot_02.png')
    mask = pygame.mask.from_surface(image_shot)
    speed = 5
    general_direction = Direction.D_LEFT
    direction = Direction.D_LEFT
    periodicity = 160
    uron = 1

    def __init__(self):
        self.periodcity_time = pygame.time.get_ticks()
        self.shots = 4
        self.is_shot = False

class Gun_superfast_ship():
    name = 'gun_main_ship'
    type = 'shot_spaceship'
    image_shot = mydef.load_image('Data/shot_02.png')
    mask = pygame.mask.from_surface(image_shot)
    speed = 6
    general_direction = Direction.D_LEFT
    direction = Direction.D_LEFT
    periodicity = 160
    uron = 1

    def __init__(self):
        self.periodcity_time = pygame.time.get_ticks()
        self.shots = 4
        self.is_shot = False

class Gun_big_ship():
    name = 'gun_big_ship'
    type = 'shot_spaceship'
    image_shot = mydef.load_image('Data/shot_03.png')
    mask = pygame.mask.from_surface(image_shot)
    speed = 6
    general_direction = Direction.D_LEFT
    direction = Direction.D_LEFT
    periodicity = 200
    uron = 3

    def __init__(self):
        self.periodcity_time = pygame.time.get_ticks()
        self.shots = 8
        self.is_shot = False




class Explosion(pygame.sprite.Sprite):
    #pygame.display.init()
    #screen = pygame.display.set_mode((10,10))  # основное окно
    KF_IMAGE = 0  # на сколько уменьшить изображение
    # словарь "Название набора" : "Загруженные кадры[]"
    TYPES = {
        0: mydef.get_load_images('Data/destruction_00', ".png", KF_IMAGE, KF_IMAGE),
        1: mydef.get_load_images('Data/destruction_01', ".png", KF_IMAGE, KF_IMAGE),
        2: mydef.get_load_images('Data/destruction_02', ".png", KF_IMAGE, KF_IMAGE),
        3: mydef.get_load_images('Data/destruction_03', ".png", KF_IMAGE, KF_IMAGE),
        4: mydef.get_load_images('Data/destruction_04', ".png", KF_IMAGE, KF_IMAGE),
        5: mydef.get_load_images('Data/destruction_05', ".png", -4, -4),
        6: mydef.get_load_images('Data/destruction_06', ".png", 0, 0)
    }

    def __init__(self, obj, is_kill):
        super().__init__(mydef.explosion_group)
        self.frames = Explosion.TYPES[obj.type_explosion] #набор кадров
        self.num_frame = 0 # текущий номер кадра
        self.image = self.frames[self.num_frame] # текущий кадр
        self.rect = self.image.get_rect()
        self.rect.centerx = obj.rect.centerx
        self.rect.centery = obj.rect.centery
        self.is_kill = is_kill

    def update(self):
        self.num_frame = (self.num_frame + 1)
        check = len(self.frames)
        if self.is_kill:
            check = len(self.frames)
        if not self.is_kill and len(self.frames)>3:
            check = 3
        if self.num_frame>= check:
            self.kill()
        else:
            self.image = self.frames[self.num_frame] # текущий кадр



class L04_Meteorit(Space_Object):
    images = mydef.get_load_images('Data/meteorits', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'meteorit'
        self.type = 'bomb'
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.mask = self.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 3
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 3 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 0 # сколько очков этот объект даст при уничтожении
        self.uron = 1

class L04_Fast_Meteorit(L04_Meteorit):
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group, x, y)
        self.name = 'fast_meteorit'
        self.speed = 4


class L04_Heavy_Meteorit(Space_Object):
    images = mydef.get_load_images('Data/meteorits2', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'heavy_meteorit'
        self.type = 'bomb'
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.mask = self.mask
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None #  оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 3 # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 0 # сколько очков этот объект даст при уничтожении
        self.uron = 1

class L04_Bonus(Space_Object):
    images = mydef.get_load_images('Data/bonuses', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])

    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.name = 'bonus'
        self.type = 'bonus'
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.mask = self.mask
        self.rect.x = x
        self.rect.y = y
        self.start_y = y
        self.last_rect = self.rect
        self.speed = 2
        self.general_direction = Direction.D_LEFT
        self.direction = Direction.D_LEFT
        self.gun = None  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 6  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 0
        self.health = self.max_health
        self.value = 300  # сколько очков содержит
        self.uron = 0

    def update(self):
        super().update()
        self.rect.y = 10 * cos(0.10 * self.num_step) + self.start_y

class L04_Bonus_big(L04_Bonus):
    images = mydef.get_load_images('Data/bonuses_big', '.png', 0, 0)
    mask = pygame.mask.from_surface(images[0])
    def __init__(self, gameboard, group, x, y):
        super().__init__(gameboard, group,x,y)
        self.name = 'bonus_big'
        self.value = 500  # сколько очков содержит