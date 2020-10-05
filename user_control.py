from public_vars import *
import glb
from mydef import *
# import sounds
import myGUI
import data_gamers
from space_objects.base import Direction
from space_objects.sounds import *
import space_objects.bombs_meteorits
import space_objects.bonuses
import space_objects.opponents
import space_objects.opponents_venera
import space_objects.opponents_mercury
import menu
import levels
from space_objects.main_ship_module import Protect_field

def pause():
    is_pause = True
    while is_pause:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                is_pause = False

class Gameover(pygame.sprite.Sprite):
    img = load_image('Data/game_over.png')
    glb.is_game_over = False

    def __init__(self):
        super().__init__(labelsprites_group)
        self.image = Gameover.img
        self.rect = self.image.get_rect()
        self.rect.center = Gameboard.rect.center

    def update(self, *args):
        pass

    @staticmethod
    def game_over():
        if not glb.is_game_over:
            stop_fone_music()
            Gameover()
            get_random_sound('Data/Sound/gameover').play()
            glb.is_game_over = True

class Level_comlete(pygame.sprite.Sprite):
    img = load_image('Data/level_complete.png')
    glb.is_level_complete = False
    font = pygame.font.Font('MagistralC.otf', 40)
    font2 = pygame.font.Font('MagistralC.otf', 50)
    path = 'Data/raiting/'
    images_reiting = []
    for i in range(6):
        file_name = path + str(i) + '.png'
        images_reiting.append(load_image(file_name, -4, -4))
    def __init__(self):
        super().__init__(labelsprites_group)
        self.image = pygame.Surface((600,400))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.image.blit (self.img, (0, 0))
        self.rect.center = Gameboard.rect.center
        self.text_result = 'Результат: '+str(glb.hero.points)
        self.text = myGUI.Text_label (self.text_result, self.font, (250,100,0), 600, 50, v=2)
        self.text.set_label(self.image, 0, 130)
        self.image_reiting = self.images_reiting[levels.get_reiting(glb.num_level, glb.hero.points)]
        x = (self.image.get_width()//2) - (self.image_reiting.get_width()//2)
        self.image.blit(self.image_reiting, (x, 190))
        play_fone_music('Data/Sound/level_complete')
        if glb.hero.points>data_gamers.get_points_of_gamer_on_level(glb.num_level):
            self.text_record = "Это твой новый рекорд!"
            self.text = myGUI.Text_label(self.text_record, self.font2, (250, 100, 0), 600, 50)
            self.text.set_label(self.image, 0, 250)



    def update(self, *args):
        pass


    @staticmethod
    def level_comlpete():
        if not glb.is_level_complete and not glb.is_game_over:
            stop_fone_music()
            Level_comlete()
            get_random_sound('Data/Sound/level_complete').play()
            glb.is_level_complete = True
            record = data_gamers.bd_gamers.get(data_gamers.get_now_gamer()).get(glb.num_level,0)
            if  glb.hero.points > record:
                data_gamers.bd_gamers[data_gamers.get_now_gamer()][glb.num_level] = glb.hero.points
                data_gamers.write_bd_gamers()
                # menu.buttons_group.empty()


def usertime():
    glb.events = pygame.event.get()
    # действия игрока
    for event in glb.events:
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            stop_fone_music()
            glb.is_level_process = False
        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            glb.hero.direction = Direction.D_STOP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            # для тестов
            pass
            # space_objects.bombs_meteorits.Meteorit_boss_pluton(900,300)
            # glb.background.is_shaking = True
            # glb.background.time_shaking = pygame.time.get_ticks()
            # Level_comlete.level_comlpete()
            #space_objects.bonuses.Bonus_shot_double(599,300)
            # space_objects.bombs_meteorits.Meteorit_boss_pluton(999,300)
            # stop_fone_music()
            # play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
            #glb.hero.protect = space_objects.main_ship_module.Protect_field(glb.hero)
            #space_objects.bombs_meteorits.Boss_Saturn(999, 200)
            # space_objects.opponents.OP_Boss_upiter(999,200)
            # space_objects.bonuses.Bonus_atom_shot(599, 300)
            space_objects.opponents_mercury.OP_Boss_merc(999,250)
            space_objects.opponents_mercury.OP_Boss_merc(999, 450)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE :
            pause_fone_music()
            pause()
            unpouse_fone_music()
        if glb.is_game_over and event.type == pygame.MOUSEBUTTONDOWN:
            glb.is_level_process = False
        if glb.is_level_complete and event.type == pygame.MOUSEBUTTONDOWN:
            glb.is_level_process = False

    glb.hero.gun.is_shooting = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        glb.hero.direction = Direction.D_RIGTH
    if keys[pygame.K_LEFT]:
        glb.hero.direction = Direction.D_LEFT
    if keys[pygame.K_DOWN]:
        glb.hero.direction = Direction.D_DOWN
    if keys[pygame.K_UP]:
        glb.hero.direction = Direction.D_UP
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        glb.hero.direction = Direction.D_RIGTH_DOWN
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        glb.hero.direction = Direction.D_RIGTH_UP
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        glb.hero.direction = Direction.D_LEFT_DOWN
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        glb.hero.direction = Direction.D_LEFT_UP
    if keys[pygame.K_SPACE]:
        glb.hero.gun.is_shooting = True