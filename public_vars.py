import pygame
import mydef


WIDTH_GAMEBOARD = 1250
HEIGHT_GAMEBOARD = 600





allsprites_group = pygame.sprite.Group()
labelsprites_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

all_bonuses = []
chance_trophy = []

# main_ship = 0

# event = None
# num_level = 0
# now_level = {}

# def init_level():
#     is_level_process = True
#     allsprites_group.empty()
#     explosion_group.empty()
#     background.Background.traversed = 0

class Gameboard():
    w, h = WIDTH_GAMEBOARD, HEIGHT_GAMEBOARD
    rect = pygame.Rect((0, 0), (w, h))  # виртуальная область игрового поля
    x = rect.x
    y = rect.y
    surf = pygame.Surface((w, h))

# class Statusboard():
#     w, h = 250, Gameboard.h
#     rect = pygame.Rect(Gameboard.rect.topright, (w, h))  # виртуальная область статус-поля
#     surf = pygame.Surface((w,h))
#     pygame.draw.rect(surf, (100,100,100), (0,0,w,h),1)
#     x = rect.x
#     y = rect.y
#
# statusboard = Statusboard()