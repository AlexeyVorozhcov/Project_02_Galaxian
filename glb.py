import random
from mydef import random_chance
from flying_objects import Flying_object, Flying_Bonus
import public_vars


events = None
num_level = 0
now_level = {}
hero = None

is_level_process = None
is_game_over = None
is_level_complete = None


background = None


def make_fly_bonus(bonus):
    x1 = 1
    y1 = 1
    type = 0
    if bonus.name =='bonus_shot' or bonus.name == 'bonus_shot_double':
        x1 =50
        y1 =50
    if bonus.name =='bonus_protect':
        x1 =50
        y1 =70
    if bonus.type == 'bonus_crystall':
        x1 = 220
        y1 = 10
        type = 1


    Flying_Bonus(type, bonus.rect.centerx, bonus.rect.centery, x1, y1, 25)


def make_trophy(obj):
    if obj.is_boss or obj.name=='upiter_04':
        for i in range(2):
            Flying_object(obj.rect.centerx, obj.rect.centery, random.randint(10,80), random.randint(100,150), 4)
            Flying_object(obj.rect.centerx, obj.rect.centery, random.randint(280, 350), random.randint(100, 150), -4)
            Flying_object(obj.rect.centerx, obj.rect.centery, random.randint(100, 170), random.randint(100, 150), 4)
            Flying_object(obj.rect.centerx, obj.rect.centery, random.randint(190, 260), random.randint(100, 150), -4)

    else:
        if obj.is_couse_trophy>0 and random.randint(1,100) < obj.is_couse_trophy:
            x = obj.rect.centerx
            y = obj.rect.centery
            random_chance (public_vars.all_bonuses, public_vars.chance_trophy)(x, y)

num_gamer = 0

# def make_tropy_crystall(x, y):
#     random.choice(troph_crystall)(x, y)