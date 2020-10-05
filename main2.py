import public_vars
import glb
from os import environ
from menu import start_main_menu
import levels
from background_game import *
from space_objects.main_ship_module import *
from space_objects.sounds import *
# import sounds
import user_control
import myGUI
import logic_game
import up_panel

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
fps = 60
font_label_shots = pygame.font.Font(None, 30)



# size = (WIDTH_GAMEBOARD, HEIGHT_GAMEBOARD) # размер окна
# environ['SDL_VIDEO_CENTERED'] = '1'
# screen = pygame.display.set_mode(size) # основное окно
# pygame.display.set_caption("Моя вторая игра на Python. Ворожцов А.В.")

# Главный цикл программы
while True:
    glb.num_level = start_main_menu(screen) # запускаем главное меню и получаем номер выбранного уровня
    glb.now_level = levels.load_level(glb.num_level) # загружаем уровень с этим номером
    speed_background = 20
    if glb.num_level == 4: speed_background = 5 # в сатурне скорость увеличена
    if glb.num_level == 10: speed_background = 40  # в солнце скорость уменьшена
    glb.background = Background(levels.get_image_background(glb.num_level), speed=speed_background) # создаем движущийся фон
    allsprites_group.empty() # очищаем спрайты
    explosion_group.empty() # очищаем спрайты
    labelsprites_group.empty()
    glb.background.traversed = 0 # устанавливаем фон в начальную позицию
    glb.hero = Main_ship(30, 150, 500) # создаем главный игровой персонаж, которым управляет игрок
    play_fone_music('Data/Sound/fon') # включаем фоновую музыку
    glb.is_level_process = True # запуск игрового цикла
    glb.is_game_over = False
    glb.is_level_complete = False
    up_panel.UP_PANEL =  up_panel.AboutLevel()

    while glb.is_level_process:
        user_control.usertime() # обработка действий игрока
        # далее отрисовка всех элементов графики
        screen.fill((0, 0, 0))
        glb.background.draw_(screen)
        allsprites_group.update()
        allsprites_group.draw(screen)
        explosion_group.update()
        explosion_group.draw(screen)

        logic_game.processing() # обработка столкновений и событий

        # далее отрисовка боковой панели
        # statusboard.surf.fill((0,0,0))
        # shots_label = myGUI.Text_label('Снаряды: '+ str(glb.hero.gun.shots), font_label_shots, (255,255,255), statusboard.w-5, 30)
        # shots_label.set_label(statusboard.surf,0,10)
        # points_label = myGUI.Text_label('Очки: ' + str(glb.hero.points), font_label_shots, (255, 255, 255),
        #                                statusboard.w - 5, 30)
        # points_label.set_label(statusboard.surf, 0, 40)
        labelsprites_group.update()
        labelsprites_group.draw(screen)
        # screen.blit(statusboard.surf, (WIDTH_GAMEBOARD, 0))


        pygame.display.flip()
        clock.tick(fps)





