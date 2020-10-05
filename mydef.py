import os
import sys
import pygame
import random
from os import environ
#

WIDTH_GAMEBOARD = 1250
HEIGHT_GAMEBOARD = 600
size = (WIDTH_GAMEBOARD, HEIGHT_GAMEBOARD) # размер окна
environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode(size) # основное окно
pygame.display.set_caption("Моя вторая игра на Python. Ворожцов А.В.")

explosion_group = pygame.sprite.Group()

def log(*args):
    print(args)

def rename_path(old_path):
    result_00 = old_path.split("/", maxsplit= -1)
    result = os.path.join(*result_00)
    return result

'''Получить список файлов в директории
dir - относительный путь
end_switch  - фильтр по расширению'''


def get_list_files(dir, end_switch):
    dir = rename_path(dir)
    files = [f for f in os.listdir(dir) if f.endswith(end_switch)]
    return files


''' Получить изображение из файла
name - имя файла
w, h - параметры изменения изображения. 
Значения Больше нуля - установить указанные размеры. 
Значения меньше нуля - изменить размеры изображения в указанное количество раз'''


def load_image(name, w=0, h=0):
    fullname = rename_path(name)
    image = pygame.image.load(fullname).convert_alpha()
    try:
        if name[-2:] == "jpg":
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Cannot load image: ', name)
        print(Exception)
        #raise SystemExit()

    if w > 0 and h > 0:
        image_result = pygame.transform.scale(image, (w, h))  # устанавливаем заданный размер
    elif w < 0 and h < 0:
        image_result = pygame.transform.scale(image, (
            image.get_width() // (-w), image.get_height() // (-h)))  # уменьшаем в w раз
    else:
        image_result = image
    print("Загрузка " + fullname)
    return image_result


''' Загрузка в список изображений: директория, расширение, 
параметры изменения изображения (см. load_image)'''


def get_load_images(directory, end_switch, w, h):
    directory = rename_path(directory)
    files = get_list_files(directory, end_switch)
    result = []
    for f in files:
        fullname = directory + '/' + f
        result.append(load_image(fullname, w, h))
    return result





# Проверка столкновения по маске объекта с любым объектом из группы
# Возвращает объект, с кем имеется столкновение. Если столкновения нет,
# возвращет проверяемый объект
def check_is_collision_by_mask(self, group):
    result = self
    for obj in group:
        if obj != self and pygame.sprite.collide_mask(obj, self):
            result = obj
    return result

def check_is_collision(self, group):
    result = self
    for obj in group:
        if obj != self and pygame.sprite.collide_rect(obj, self):
            result = obj
    return result

def check_is_collision_on_list(self, group):
    result = []
    for obj in group:
        if obj != self and pygame.sprite.collide_rect(obj, self):
            result.append(obj)
    return result


# Проверка 3D столкновения объекта с любым объектом из группы
# Возвращает объект, с кем имеется столкновение. Если столкновения нет,
# возвращет проверяемый объект
def check_is_collision_by_3d (self, group):
    obj = check_is_collision_by_mask(self, group)
    result = self
    if self!=obj:
        if self.rect.bottom - self.framing < obj.rect.bottom:  # подход сверху
           if obj.rect.bottom - obj.fat <= self.rect.bottom - self.framing:
               result = obj  # герой подходит сверху
        if self.rect.bottom - self.framing >= obj.rect.bottom:  # подход снизу
           if self.rect.bottom - self.fat <= obj.rect.bottom - obj.framing:
               result = obj  # герой подходит снизу
    return result

def check_timer (start_time, action_time):
    if pygame.time.get_ticks()-start_time >= action_time: return True
    else: return False

def get_event(sprite, event):
    result = False
    if sprite.rect.collidepoint(event.pos):
        result=True
    return result

def check_click(pos, obj, vx, vy):
    if pos[0] >= obj.rect.x+vx and pos[0] <= obj.rect.right+vx and \
        pos[1] >= obj.rect.y + vy and pos[1] <= obj.rect.bottom+vy:
        print (obj.rect.x+vx, obj.rect.right+vx )
        return True
    else: return False

def random_chance(list, weights):
    result = None
    if len(list) != len(weights):
        print ('Ошибка: списки не равны!')
        for i in range(len(list) - len(weights)):
            weights.append(0)
    sum = 0
    list_b = [1]
    for i in weights:
        sum += i
        list_b.append(sum)
    # print(sum)
    r = random.randint(1, sum-1)
    for i in range(len(list_b)-1):
        if list_b[i] <= r and r<list_b[i+1]:
            result = list[i]
    if result== None:
        print ()
    return result


def terminate():
    pygame.quit()
    sys.exit()


