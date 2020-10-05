from space_objects.bombs_meteorits import *
from space_objects.bonuses import *
from space_objects.opponents import *
from random import randint
from space_objects.opponents_02 import *
from space_objects.opponents_venera import *
from space_objects.opponents_mercury import *
from space_objects.opponent_sun import *

def get_image_background(num):
    return load_image(level_dict[num].file_background)

# установить определенный объект в определенную точку
def get_object_on_level_in_point(point, y, obj):
    new_objects = []
    new_objects.append([range(point, point+1),[0, y], [obj], [100]])
    return new_objects

# разместить объекты полосой друг за другом
def get_object_on_level_in_line(point, y, kol, distance, obj):
    new_objects = []
    for i in range(kol):
        new_objects.append([range(point + i*distance, point + i*distance + 1 ), [0, y], [obj], [100]])
    return new_objects

# разместить объекты по диагонали
def get_object_on_level_in_diagonal(point, y, kol, distanceY, distanceX, obj):
    new_objects = []
    k = 0
    for i in range(point, point+kol*distanceX, distanceX):
        new_objects.append([range(i, i + 1), [0, y + k*distanceY], [obj], [100]])
        k += 1
    return new_objects

# разместить объекты клином
def get_object_on_level_in_wedge(point, y, kol, distanceY, distabceX, obj):
    new_objects = []
    new_objects.extend(get_object_on_level_in_diagonal(point + distabceX, y - distanceY, kol - 1, -distanceY, distabceX, obj))
    new_objects.append([range(point, point+1), [0, y], [obj], [100]])
    new_objects.extend(get_object_on_level_in_diagonal(point + distabceX+1, y + distanceY, kol - 1, distanceY, distabceX, obj))
    return new_objects

# разместить объекты ромбом
def get_object_on_level_in_romb(point, y, kol, distanceY, distabceX, obj):
    new_objects = []
    new_objects.extend(get_object_on_level_in_wedge(point + distabceX, y - distanceY, kol//2 - 1, -distanceY, distabceX, obj))
    new_objects.extend(get_object_on_level_in_wedge(point + distabceX*(kol-2), y - distanceY, kol//2 - 1, -distanceY, -distabceX, obj))
    return new_objects

# разместить объекты ромбом, а внутри ромба бонус
def get_object_on_level_in_romb_with_bonus(point, y, kol, distanceY, distabceX, obj, bonus):
    new_objects = []
    new_objects.extend(get_object_on_level_in_romb(point, y, kol, distanceY, distabceX, obj))
    new_objects.append([range(point+(kol//2)*distabceX-1, point+(kol//2)*distabceX), [0, y-distanceY], [bonus], [100]])
    # bonus.speed = obj.speed
    return new_objects


class Lev_01():
    is_ready = True
    name = 'ПЛУТОН'
    data_reiting = [500,1000,2000,3000,4000]
    file_background = 'Data/level_pluton.jpg'
    comb = [ Meteorit_01,
             Meteorit_02,
             Bonus_shot,
             Bonus_health,
             Bonus_protect,
             Meteorit_boss_pluton,
             Bonus_crystall_small]
    level = []
    level.append([range(1, 100), [970, 30], comb, [100, 0, 0, 0, 0, 0, 0]])
    level.append([range(101, 500), [960, 40], comb, [50, 20, 1, 1, 1, 0, 1]])
    level.append([range(501, 1000), [930, 70], comb, [50, 20, 1, 1, 1, 0, 1]])
    level.append([range(1001, 2000), [910, 90], comb, [50, 20, 1, 1, 1, 0, 1]])
    level.append([range(2061, 2300), [930, 70], comb, [0, 0, 2, 2, 2, 0, 2]])
    level.extend(get_object_on_level_in_point(2301, 200, Meteorit_boss_pluton))
    level.append([range(2400, 2500), [960, 40], comb, [50, 20, 10, 5, 5, 0, 10]])

class Lev_02():
    is_ready = True
    name = 'НЕПТУН'
    data_reiting = [1000, 2000, 5000, 7000, 8000]
    file_background = 'Data/level_neptun.jpg'
    comb = [Bomb_01,
            OP_01_neptun,
            OP_02_neptun,
            OP_03_neptun,
            OP_04_neptun,
            Bonus_shot,
            Bonus_health,
            Bonus_protect,
            Bonus_crystall_small,
            Bonus_shot_double
    ]
    level = []

    level.extend(get_object_on_level_in_diagonal(50, 100, 10, 20, 10, OP_01_neptun))
    level.extend(get_object_on_level_in_diagonal(200, 500, 10, -20, 10, OP_01_neptun))
    level.extend(get_object_on_level_in_wedge   (350, 300, 10, 20, 15, OP_01_neptun))
    # level.extend(get_object_on_level_in_romb_with_bonus(550, 300, 10, 20, 5, OP_01_neptun, Bonus_crystall_small))
    level.append([range(500, 730), [920, 80], comb, [50, 50, 0, 0, 0, 0, 0, 0, 1]])
    level.append([range(730, 1200), [920, 80], comb, [50, 50, 30, 0, 0, 0, 0, 0, 1]])
    level.append([range(1201, 2000), [920, 80], comb, [30, 70, 0, 0, 1, 0, 0, 0, 1]])
    level.append([range(2001, 2500), [920, 80], comb, [5, 50, 50, 0, 0, 1, 1, 1, 1]])
    level.append([range(2450, 2451), [0, 250], comb, [0, 0, 0, 0, 0, 0, 0, 0, 0, 100]])
    level.append([range(2452, 2453), [0, 450], comb, [0, 0, 0, 0, 0, 0, 0, 0, 0, 100]])
    level.append([range(2501, 2800), [920, 80], comb, [0, 20, 60, 30, 20, 1, 1, 1, 1, 3]])
    level.append([range(2801, 3000), [920, 70], comb, [0, 0, 0, 10, 100, 0, 0, 5, 1, 3]])
    level.append([range(3001, 3200), [900, 100], comb, [100, 100, 100, 100, 5, 5, 5, 30, 10, 10]])

class Lev_03():
    is_ready = True
    name = 'УРАН'
    data_reiting = [3000, 5000, 8000, 10000, 12000]
    file_background = 'Data/level_uran.jpg'
    comb = [Bomb_01,
            Bomb_02,
            OP_01_uran01,
            OP_02_uran02,
            OP_03_uran02,
            OP_04_uran02,
            Bonus_shot,
            Bonus_health,
            Bonus_protect,
            Bonus_shot_double,
            Bonus_crystall_small,
            Bonus_crystall_big,
            OP_boss_uran2]
    level = []
    level.append([range(1, 100), [970, 30], comb, [100, 0, 0, 0, 0, 0, 2, 0, 10, 0, 0, 0, 0]])
    level.append([range(101, 300), [960, 40], comb, [20, 5, 60, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0]])
    level.extend(get_object_on_level_in_diagonal(310,50, 10, 50, 5, OP_01_uran01))
    level.extend(get_object_on_level_in_diagonal(360, 550, 10, -50, 5, OP_01_uran01))
    level.append([range(401, 1000), [960, 40], comb, [5, 1, 60, 20, 0, 0, 2, 2, 2, 2, 2, 1, 0]])
    level.append([range(1001, 2000), [960, 40], comb, [0, 1, 20, 60, 10, 0, 2, 2, 2, 2, 2, 1, 0]])
    level.append([range(2001, 2200), [970, 30], comb, [0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0]])
    level.append([range(2201, 3000), [970, 30], comb, [5, 0, 0, 0, 50, 50, 0, 5, 5, 2, 0, 0, 0]])
    level.append([range(3001, 3500), [970, 30], comb, [0, 0, 0, 0, 50, 100, 1, 6, 5, 2, 2, 1, 0]])
    level.append([range(3501, 4000), [970, 30], comb, [5, 2, 0, 30, 30, 40, 1, 6, 5, 2, 2, 1, 0]])
    level.extend(get_object_on_level_in_point(4001, 300, OP_boss_uran2))
    # level.append([range(4001, 4002), [0, 300], comb, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]])
    level.append([range(4200, 4300), [940, 60], comb, [5, 2, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 0]])

class Lev_04():
    is_ready = True
    name = 'САТУРН'
    data_reiting = [100, 2000, 3000, 5000, 7000]
    file_background = 'Data/level_saturn.jpg'
    comb = [Fast_Meteorit_01,
            Fast_Meteorit_02,
            Bonus_shot,
            Bonus_health,
            Bonus_protect,
            Bonus_shot_double,
            Bonus_crystall_small,
            Boss_Saturn]
    level = []
    level.append([range(1, 100), [970, 30], comb, [0, 100, 0, 1, 1,0, 2]])
    level.append([range(101, 500), [920, 80], comb, [0, 100, 0, 3, 1,0, 2]])
    level.append([range(501, 2200), [910, 90], comb, [100, 100, 0, 2, 1, 0, 2]])
    level.append([range(2201, 3000), [850, 150], comb, [50, 50, 0, 2, 1, 0, 2]])
    level.append([range(3001, 3500), [800, 200], comb, [50, 50, 1, 2, 1, 2, 2]])
    # level.append([range(2550, 2551), [0, 250], comb, [0, 0, 100, 0, 0, 0, 2, 2]])
    level.extend(get_object_on_level_in_point(3550, 150, Boss_Saturn))
    level.extend(get_object_on_level_in_point(4200, 250, Boss_Saturn))
    level.extend(get_object_on_level_in_point(5050, 300, Boss_Saturn))
    # level.append([range(2601, 2602), [0, 150], comb, [0, 0, 0, 0, 0, 0, 0, 100]])
    # level.append([range(3002, 3003), [0, 250], comb, [0, 0, 0, 0, 0, 0, 0, 100]])
    # level.append([range(3402, 3403), [0, 200], comb, [0, 0, 0, 0, 0, 0, 0, 100]])


class Lev_05():
    is_ready = True
    name = 'ЮПИТЕР'
    data_reiting = [2000, 3000, 6000, 8000, 10000]
    file_background = 'Data/level_jupiter.jpg'
    comb = [Bomb_01,
            OP_01_neptun,
            OP_01_uran01,
            OP_03_upiter_05,
            OP_04_upiter_05,
            Bonus_shot,
            Bonus_health,
            Bonus_protect,
            Bonus_shot_double,
            Bonus_crystall_small,
            Bonus_crystall_big,
            OP_Boss_upiter]
    level = []
    level.extend(get_object_on_level_in_line(3, 100, 10, 10, OP_01_neptun))
    level.extend(get_object_on_level_in_line(1, 300, 10, 10, OP_01_uran01))
    level.extend(get_object_on_level_in_line(4, 500, 10, 10, OP_01_neptun))
    level.extend(get_object_on_level_in_wedge(120, 300, 20, 15, 5, OP_01_uran01))
    level.append([range(250, 400), [950, 50], comb, [99, 0, 0, 0, 1, 0, 0]])
    level.append([range(401, 500), [960, 40], comb, [10, 80, 0, 0, 0, 1, 0]])
    level.append([range(501, 1200), [950, 50], comb, [10, 50, 50, 1, 1, 1, 1, 0, 0,0,0,0]])
    level.append([range(1201, 2000), [960, 40], comb, [0, 0, 0, 100, 0, 1, 1, 5, 1,1,0,0]])
    level.append([range(2001, 2500), [960, 40], comb, [0, 0, 0, 90, 5, 1, 1, 5, 1,1,1,0]])
    level.append([range(2501, 3000), [960, 40], comb, [10, 0, 0, 90, 5, 1, 1, 5, 1,1,1,0]])
    level.append([range(3000, 3500), [950, 50], comb, [10, 50, 5, 5, 1, 1, 1, 1, 1,1,1,0]])
    level.append([range(3500, 3700), [930, 70], comb, [0, 50, 50, 1, 1, 1, 1, 1, 1,1,1,0]])
    level.extend(get_object_on_level_in_point(3790, 200, OP_Boss_upiter))
    # level.append([range(3790, 3791), [0, 200], comb, [0, 0, 0, 0, 0, 2, 0, 0, 0,0,0,100]])

class Lev_06():
    is_ready = True
    name = 'МАРС'
    file_background = 'Data/level_mars.jpg'
    data_reiting = [2000, 10000, 13000, 18000, 20000]
    comb = [Bomb_01,
            Bomb_02,
            OP_01_Mars,
            OP_02_Mars,
            OP_03_Mars,
            OP04_Mars,
            OP05_Mars,
            OP_06_Mars,
            Bonus_shot_fast]

    level = []
    level.append([range(1, 99), [970, 30], comb, [30,30, 40 , 0, 0, 0, 0, 0]])
    level.extend(get_object_on_level_in_line(100, 300, 5, 10, OP_01_Mars))
    level.append([range(150, 549), [910, 90], comb, [10, 10, 80, 0, 0, 0]])
    level.extend(get_object_on_level_in_wedge(510, 300, 10 , 15, 15 , OP_02_Mars))
    level.append([range(550, 1200), [940, 60], comb, [10, 0, 80, 10, 0, 0]])
    level.append([range(1201, 2000), [970, 30], comb, [10, 0, 70, 10, 10, 0, 0, 5]])
    level.append([range(2001, 2500), [920, 80], comb, [0, 5, 75, 10, 10, 5]])
    level.extend(get_object_on_level_in_point(2100, 300, Bonus_health))
    level.append([range(2501, 3000), [970, 30], comb, [0, 0, 70, 10, 10, 10, 5]])
    level.append([range(3100, 4000), [960, 40], comb, [0, 0, 70, 10, 10, 10, 5]])
    level.extend(get_object_on_level_in_point(3100, 300, Bonus_health))
    level.extend(get_object_on_level_in_point(3200, 200, OP05_Mars))
    level.extend(get_object_on_level_in_point(3600, 300, OP05_Mars))
    level.extend(get_object_on_level_in_point(3700, 300, Bonus_health))
    level.extend(get_object_on_level_in_point(3800, 400, OP05_Mars))
    level.extend(get_object_on_level_in_point(4099, 250, OP05_Mars))
    level.append([range(4100, 4800), [960, 40], comb, [0, 0, 0, 0, 0, 0, 0, 100]])
    level.append([range(4801, 5000), [900, 100], comb, [10, 0, 0, 0, 0, 0, 0, 90, 5]])
    level.extend(get_object_on_level_in_point(5050, 250, OP_06_Boss_mars))

class Lev_07():
    is_ready = True
    name = 'ЗЕМЛЯ'
    file_background = 'Data/level_earth.jpg'
    data_reiting = [5000, 15000, 18000, 20000, 25000]
    comb = [OP_01_Earth,
            OP_02_Earth,
            OP_03_Earth,
            OP_04_Earth,
            OP_05_Earth,
            Bonus_shot,
            Bonus_shot_double,
            Bonus_health,
            Bonus_protect,
            Bonus_shot_fast
            ]

    level = []
    level.append([range(0, 100), [970, 30], comb, [100, 0, 0, 0, 0]])
    level.append([range(101, 500), [960, 40], comb, [100, 20, 0, 0, 0, 0,2,0,0]])
    level.append([range(501, 900), [960, 40], comb, [20, 80, 0, 0, 0, 1,2,1,0]])
    level.append([range(901, 1200), [960, 40], comb, [0, 0, 100, 0, 0, 1, 2, 1, 2]])
    level.append([range(1201, 1800), [970, 30], comb, [5, 10, 30, 5, 2, 1,2,1,2,1]])
    level.append([range(1801, 2000), [970, 30], comb, [0, 0, 0, 100, 2, 1, 5, 1, 2,1]])
    level.extend(get_object_on_level_in_point(1999, 400, Bonus_atom_shot))
    level.append([range(2001, 2200), [960, 40], comb, [0, 0, 0, 90, 10, 1, 5,2,2,1]])
    level.append([range(2201, 2400), [980, 20], comb, [0, 0, 0, 0, 100, 1, 5, 2, 2,1]])
    level.append([range(2401, 2500), [900, 100], comb, [50, 50, 10, 10, 10, 1, 2, 2, 2]])
    level.extend(get_object_on_level_in_point(2550, 100, OP_stantion_Earth))
    level.extend(get_object_on_level_in_point(2580, 200, OP_stantion_Earth))
    level.extend(get_object_on_level_in_point(2610, 350, OP_stantion_Earth))
    level.extend(get_object_on_level_in_point(2650, 450, OP_stantion_Earth))
    level.append([range(2750, 3400), [970, 30], comb, [100, 0, 0, 0, 0, 0, 2, 5, 0,1]])
    level.extend(get_object_on_level_in_point(3000, 200, OP_boss1_Earth))

class Lev_08():
    is_ready = True
    name = 'ВЕНЕРА'
    data_reiting = [5000, 10000, 15000, 18000, 20000]
    file_background = 'Data/level_venera.jpg'
    comb = [OP_01_Mars,
            OP_02_Mars,
            OP_03_Venera,
            OP_04_Venera,
            Bonus_health,
            Bonus_protect,
            Bonus_shot_fast,
            Bonus_atom_shot,
            Bonus_crystall_small,
            Bonus_crystall_big]
    level = []
    level.append([range(1, 250), [970, 30], comb, [100]])
    level.append([range(251, 700), [900, 100], comb, [100]])
    level.append([range(701, 1200), [960, 40], comb, [50, 50]])
    level.append([range(1201, 1600), [940, 60], comb, [0, 100, 0,0,2,5,1,1,2,2]])
    level.append([range(1601, 2000), [950, 50], comb, [0, 50, 50,0,2,5,1,1,2,2]])
    level.append([range(2001, 2300), [950, 50], comb, [0, 0, 100,0,2,5,1,1,2,2]])
    level.append([range(2301, 2600), [960, 40], comb, [0, 0, 0, 100,2,5,1,1,2,2]])
    level.append([range(2601, 3000), [950, 50], comb, [10, 20, 50, 20,2,5,1,1,2,2]])
    level.extend(get_object_on_level_in_diagonal(2800, 350, 5, 15, 20, Bonus_health))
    level.extend(get_object_on_level_in_diagonal(2900, 500, 5, 15, 20, Bonus_protect))
    level.extend(get_object_on_level_in_point(3050, 200, OP_boss_Venera))
    level.append([range(3100, 3550), [960, 40], comb, [100]])
    level.append([range(3551, 3850), [960, 40], comb, [100, 100]])

    # level.append([range(501, 1200), [950, 50], comb, [100, 0, 0, 0, 0, 0, 0]])
    # # level.append([range(1201, 2000), [940, 60], comb, [95, 2, 2, 0, 0, 0, 0]])
    # # level.append([range(2001, 2500), [930, 70], comb, [95, 2, 2, 0, 0, 0, 0]])
    # # level.append([range(2501, 3000), [920, 80], comb, [87, 5, 2, 0, 5, 0, 0]])
    # # level.append([range(3000, 3500), [870, 130], comb, [82, 5, 2, 1, 10, 0, 0]])
    # level.append([range(500, 1000), [900, 100], comb, [72, 5, 2, 1, 20, 0, 0]])
    # level.append([range(801, 802), [0, 200], comb, [0, 0, 0, 0, 0, 100, 0]])

class Lev_09():
    is_ready = True
    name = 'МЕРКУРИЙ'
    data_reiting = [5000, 10000, 15000, 20000, 23000]
    file_background = 'Data/level_mercury.jpg'
    comb = [Bonus_shot_fast,
            Meteorit_01,
            OP_01_Mer,
            OP_02_Mer,
            OP_03_Mer,
            Bonus_health,
            Bonus_protect,
            Bonus_atom_shot]
    level = []
    level.append([range(1, 100), [970, 30], comb, [0, 100]])
    level.extend(get_object_on_level_in_point(99, 200, Bonus_shot_fast))
    level.append([range(101, 500), [960, 40], comb, [10, 50, 50, 0, 0, 5]])
    level.append([range(501, 1200), [900, 100], comb, [10, 20, 50, 20, 0, 10, 2]])
    level.append([range(1201, 2000), [960, 40], comb, [10, 20, 0, 100, 0, 10, 10, 2]])
    level.append([range(2001, 2500), [930, 70], comb, [5, 0, 100, 0, 5, 10, 10, 2]])
    level.append([range(2501, 3000), [920, 80], comb, [5, 10, 0, 0, 95, 10, 10]])
    level.extend(get_object_on_level_in_point(3100, 250, OP_Boss_merc))
    level.extend(get_object_on_level_in_point(3101, 450, OP_Boss_merc))

    # # level.append([range(3000, 3500), [870, 130], comb, [82, 5, 2, 1, 10, 0, 0]])
    # level.append([range(500, 1000), [900, 100], comb, [72, 5, 2, 1, 20, 0, 0]])
    # level.append([range(801, 802), [0, 200], comb, [0, 0, 0, 0, 0, 100, 0]])

class Lev_10():
    is_ready = True
    name = 'СОЛНЦЕ'
    data_reiting = [5000, 10000, 15000, 20000, 23000]
    file_background = 'Data/level_sun.jpg'
    # comb = [Bonus_shot_fast,
    #         Meteorit_01,
    #         OP_01_Mer,
    #         OP_02_Mer,
    #         OP_03_Mer,
    #         Bonus_health,
    #         Bonus_protect,
    #         Bonus_atom_shot]
    level = []
    level.extend(get_object_on_level_in_point(50, 300, OP_Sun_Uran))

level_dict = {
    1:Lev_01,
    2:Lev_02,
    3:Lev_03,
    4:Lev_04,
    5:Lev_05,
    6:Lev_06,
    7:Lev_07,
    8:Lev_08,
    9:Lev_09,
    10:Lev_10
}


# загрузка и возврат нужного уровня num
def load_level (num):
    result = None
    if level_dict.get(num) != None and level_dict[num].is_ready:
        min_y = 2
        max_y = HEIGHT_GAMEBOARD-40
        result= {}
        for part in level_dict[num].level:
            for distance in part[0]:
                if part[1][0] == 0:
                        result[distance] = [mydef.random_chance(part[2], weights=part[3]), part[1][1]]
                else:
                    if mydef.random_chance([False, True], part[1]):
                        result[distance] = [mydef.random_chance(part[2], weights=part[3]), randint(min_y, max_y)]

    return result

def get_reiting(n, points):
    result = 0
    if level_dict.get(n).is_ready != False:
        list_reiting = level_dict[n].data_reiting
        i=0
        for point_level in list_reiting:
            i+=1
            if points>=point_level:
                result=i
    return result

#print (get_reiting(1, 3500))
#print (level_dict[2])

def get_image_background(num):
    return mydef.load_image(level_dict[num].file_background)

def get_name_level():
    return level_dict[glb.num_level].name