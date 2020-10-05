from public_vars import *
import glb
from space_objects.main_ship_module import *
from space_objects.bonuses import *
import user_control
from mydef import random_chance

def check_level_complete():
    # print('Количество спрайтов:' + str(len(allsprites_group)))
    # print ('Protect: ' + str(str(glb.hero.protect)))
    if glb.hero.protect!= None:
        print ('Protect Health: ' + str(glb.hero.protect.health) )
    print ('Остаток объектов в уровне: ' + str(len(glb.now_level)))
    if glb.hero.protect == None:
        protect_health=0
    else:
        protect_health = glb.hero.protect.health
    result = False
    if len(glb.now_level) == 0 and len(allsprites_group) == 2:
        result = True
    if len(glb.now_level) == 0 and len(allsprites_group) == 3 and protect_health>0:
        result = True

    return result

def make_opponent(num):
    if glb.now_level.get(num) != None:
        obj = glb.now_level[num][0]
        pos_y = glb.now_level[num][1]
        temp = glb.now_level.pop(num)
        making_obj = obj(WIDTH_GAMEBOARD, pos_y)
        if making_obj.is_boss:
            stop_fone_music()
            play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку



def processing():
    print (len(public_vars.explosion_group))
    for obj in public_vars.explosion_group:
        print ('проверка explosion')
        if obj.type == 'atom_shot':
            objects_col = mydef.check_is_collision_on_list(obj, allsprites_group)
            for obj_col in objects_col:
                if obj_col.type == 'opponent' or obj_col.type == 'bomb' or obj_col.type=='shot opponent':
                    obj.master.master.points += obj_col.to_destruction(uron=obj.damage)

    for obj in allsprites_group:
        if obj.type != 'shot_main' and obj.type != 'shot opponent':
            obj_col = mydef.check_is_collision_by_mask(obj, allsprites_group)
            if obj_col != obj:
                if obj.type == 'opponent'  and obj_col.type == 'shot_main':
                    obj_col.master.master.points += obj.to_destruction(obj_col.damage)
                    trash = obj_col.to_destruction(obj_col.health)

                if obj.type == 'bomb' and obj_col.type == 'shot_main':
                    obj_col.master.master.points += obj.to_destruction(obj_col.damage)
                    trash = obj_col.to_destruction(obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.type == 'bomb':
                    obj.points += obj_col.to_destruction(uron=obj.damage)
                    trash = obj.to_destruction(uron=obj_col.damage)
                if obj.type == 'main_spaceship' and obj_col.type == 'opponent':
                    obj.points += obj_col.to_destruction(uron=obj.damage)
                    trash = obj.to_destruction(obj_col.damage)

                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_shot':
                    obj.gun = G01_standart(obj, obj.gun.shots)
                    obj.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_shot_double':
                    obj.gun = G02_double(obj, obj.gun.shots)
                    obj.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_shot_fast':
                    obj.gun = G03_fast(obj, obj.gun.shots)
                    obj.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_atom_shot':
                    obj.gun = G04_Atom(obj, obj.gun.shots)
                    trash = obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_health':
                    obj.health = obj.max_health
                    obj.points += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.type == 'bonus_crystall':
                    obj.points += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'main_spaceship' and obj_col.name == 'bonus_protect':
                    obj.points += obj_col.to_destruction(uron=obj_col.health)
                    obj.protect = Protect_field(obj)


                if obj.type == 'main_spaceship' and obj_col.type == 'shot opponent':
                    trash = obj.to_destruction(uron=obj_col.damage)
                    trash = obj_col.to_destruction(uron=obj_col.health)

                if obj.type == 'protect_field' and obj_col.type == 'shot opponent':
                    obj.master.points += obj_col.to_destruction(uron=obj_col.health)
                    trash = obj.to_destruction(uron=1)
                if obj.type == 'protect_field' and obj_col.type == 'opponent':
                    obj.master.points += obj_col.to_destruction(uron=obj.damage)
                    trash = obj.to_destruction()
                if obj.type == 'protect_field' and obj_col.type == 'bomb':
                    obj.master.points += obj_col.to_destruction(uron=obj.damage)
                    trash = obj.to_destruction()
                if obj.type == 'protect_field' and obj_col.name == 'bonus_shots':
                    obj.master.gun = G01_standart(obj.master, obj.master.gun.shots)
                    obj.master.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'protect_field' and obj_col.name == 'bonus_shot_double':
                    obj.master.gun = G02_double(obj.master, obj.master.gun.shots)
                    obj.master.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'protect_field' and obj_col.name == 'bonus_shot_fast':
                    obj.master.gun = G03_fast(obj.master, obj.master.gun.shots)
                    obj.master.gun.shots += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'protect_field' and obj_col.name == 'bonus_atom_shot':
                    obj.master.gun = G04_Atom(obj, obj.master.gun.shots)
                    trash = obj_col.to_destruction(uron=obj_col.health)


                if obj.type == 'protect_field' and obj_col.name == 'bonus_health':
                    obj.master.health = obj.master.max_health
                    obj.master.points += obj_col.to_destruction(uron=obj_col.health)
                if obj.type == 'protect_field' and obj_col.name == 'bonus_protect':
                    obj.health += 1
                    trash = obj_col.to_destruction(uron=obj_col.health)

        if obj.type == 'main_spaceship':
            if obj.gun.shots <= 10 and obj.help_shots > 0:
                Bonus_shot(WIDTH_GAMEBOARD, randint(50, 550))
                obj.help_shots -= 1
            if obj.health <= 0 and not glb.is_game_over:
                print('GAME OVER')
                user_control.Gameover.game_over()





