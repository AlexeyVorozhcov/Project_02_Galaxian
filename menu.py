from public_vars import *
import glb
from mydef import load_image, check_timer
from data_gamers import *
import myGUI
from random import randint
from levels import get_reiting, level_dict
from space_objects.sounds import *

image_name_game = load_image('Data/name_game.png', 360, 120)
file_BG = 'Data/Main menu.jpg'
image_bg = load_image(file_BG)
bg_group = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()
kol_levels = 10
name_gamer = ''
make_new_gamer = ''
del_gamer = ''

pygame.font.init()
font_name_gamer = pygame.font.Font('MagistralC.otf', 50)
font_make_gamer = pygame.font.Font('MagistralC.otf', 25)

class NameGame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(buttons_group)
        self.image = image_name_game
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 20


    def update(self, *args):
        pass





class NameGamer(pygame.sprite.Sprite):
    all_gamers = get_all_gamers()
    @staticmethod
    def get_image_name_gamer():
        print(str(glb.num_gamer))
        if glb.num_gamer+1 > len(NameGamer.all_gamers): glb.num_gamer=1
        print(NameGamer.all_gamers[glb.num_gamer])
        return myGUI.to_make_surf_from_text(" Играет: " + NameGamer.all_gamers[glb.num_gamer] +" ", font_name_gamer, (255, 255, 255))

    def __init__(self, screen):
        super().__init__(buttons_group)
        self.image = NameGamer.get_image_name_gamer()
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH_GAMEBOARD - 50
        self.rect.y = 50
        self.screen = screen

    def update(self, *args):
        pass

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            print("Нажатие на имя")
            glb.num_gamer += 1
            if glb.num_gamer >= len(bd_gamers): glb.num_gamer = 0
            write_last_gamer()
            self.image = NameGamer.get_image_name_gamer()
            self.rect = self.image.get_rect()
            self.rect.right = WIDTH_GAMEBOARD - 50
            self.rect.y = 50
            print (get_now_gamer())
            buttons = []
            for i in range(1, kol_levels + 1):
                buttons.append(Buttons_menu(self.screen, i))

class MakeNewGamer(pygame.sprite.Sprite):
    text0 = 'Добавить нового игрока'
    @staticmethod
    def get_image_label(text):
        return myGUI.to_make_surf_from_text(text, font_make_gamer,
                                            (255, 255, 255))
    def __init__(self, screen):
        super().__init__(buttons_group)
        self.image = MakeNewGamer.get_image_label(self.text0)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH_GAMEBOARD - 60
        self.rect.bottom = HEIGHT_GAMEBOARD - 470
        self.vx = 0
        self.vx_max = 30
        self.vx_speed = 8
        self.screen = screen
        self.is_sdvig = False
        self.is_input = False
        self.period_slash = 200
        self.time_period_slash = pygame.time.get_ticks()
        self.is_slash = False
        self.input_string = ''

    def eventing(self, event):
        if event.key == pygame.K_RETURN:
            add_new_gamer(self.input_string)
            self.input_string = ''
            self.is_sdvig = True
            global name_gamer
            NameGamer.all_gamers = get_all_gamers()
            name_gamer.image = NameGamer.get_image_name_gamer()
            name_gamer.rect = name_gamer.image.get_rect()
            name_gamer.rect.right = WIDTH_GAMEBOARD - 50
            name_gamer.rect.y = 50
            buttons = []
            for i in range(1, kol_levels + 1):
                buttons.append(Buttons_menu(self.screen, i))
        elif event.key == pygame.K_BACKSPACE:
            self.input_string = self.input_string[:-1]
        else:
            self.input_string += event.unicode

    def update(self, *args):
        if self.is_sdvig and not self.is_input and self.vx < self.vx_max:
            self.vx+=1
            self.rect = self.rect.move(-self.vx_speed, 0)
            if self.vx == self.vx_max:
                self.is_sdvig = False
                self.is_input = True
        if self.is_sdvig and self.is_input and self.vx > 0:
            self.vx -= 1
            self.rect = self.rect.move(self.vx_speed, 0)
            if self.vx == 0:
                self.is_sdvig = False
                self.is_input = False
                self.image = MakeNewGamer.get_image_label(self.text0)
        if self.is_input and not self.is_sdvig:
            if check_timer(self.time_period_slash, self.period_slash):
                self.is_slash = not self.is_slash
                if self.is_slash: slash = '|'
                else: slash = ''
                text = self.text0 + ': ' + self.input_string + slash
                self.image = MakeNewGamer.get_image_label(text)
                self.time_period_slash = pygame.time.get_ticks()

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if not self.is_sdvig and not self.is_input:
                self.is_sdvig = True

            if self.is_input and not self.is_sdvig:
                self.is_sdvig = True

class Del_gamer(MakeNewGamer):
    text0 = 'Удалить текущего игрока?'
    def __init__(self, screen):
        super().__init__(screen)
        self.image = MakeNewGamer.get_image_label(self.text0)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH_GAMEBOARD - 50
        self.rect.bottom = HEIGHT_GAMEBOARD - 12

    def eventing(self, event):
        if event.key == pygame.K_RETURN and self.input_string=='ДА':
            del_gamer_from_base(get_now_gamer())
            self.input_string = ''
            self.is_sdvig = True
            global name_gamer
            NameGamer.all_gamers = get_all_gamers()
            name_gamer.image = NameGamer.get_image_name_gamer()
            name_gamer.rect = name_gamer.image.get_rect()
            name_gamer.rect.right = WIDTH_GAMEBOARD - 50
            name_gamer.rect.y = 50
            buttons = []
            for i in range(1, kol_levels + 1):
                buttons.append(Buttons_menu(self.screen, i))
        elif event.key == pygame.K_BACKSPACE:
            self.input_string = self.input_string[:-1]
        else:
            self.input_string += event.unicode

class Bg_menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(bg_group)
        self.image = image_bg
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.direction = (0, -1)
        self.speed = 60
        self.time_speed = pygame.time.get_ticks()

    def update(self, *args):
        if check_timer(self.time_speed, self.speed):
            self.rect = self.rect.move(self.direction)
            self.time_speed = pygame.time.get_ticks()
            if self.rect.bottom < 600:
                self.direction = (0, 1)
            if self.rect.y > 0:
                self.direction = (0, -1)

class Reiting(pygame.sprite.Sprite):
    path = 'Data/raiting/'
    images = []
    for i in range(6):
        file_name = path + str(i) + '.png'
        images.append(load_image(file_name, -6, -6))
    def __init__(self, obj, rei):
        super().__init__(buttons_group)
        gamer = get_now_gamer()
        points_on_level = bd_gamers.get(gamer).get(obj.number)

        if points_on_level == None:
            points_on_level = 0
        self.image = Reiting.images[get_reiting(obj.number, points_on_level)]
        self.rect = self.image.get_rect()
        self.obj = obj
        self.rect.x = obj.rect.x
        self.rect.y = obj.rect.bottom + 1

    def update(self, *args):
        pass

class Data_result(pygame.sprite.Sprite):
    font = pygame.font.Font('MagistralC.otf', 15)
    def __init__(self, obj):
        super().__init__(buttons_group)
        self.obj = obj
        self.image = pygame.Surface((200,50))
        #pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 200, 50), 1)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = obj.rect.x
        self.rect.y = obj.reiting.rect.bottom + 1
        liders = get_liders(self.obj.number)
        i=0
        for lider in liders:
            color1 = (255,255,255)
            if lider[0] == get_now_gamer(): color1 = (200,200,0)
            text = (myGUI.Text_label(lider[0] + " : " + str(lider[1]), Data_result.font, color1, self.rect.width, 12, v=1))
            text.set_label(self.image, 5, i*15+3)
            i += 1

    def update(self, *args):
        pass



class Closed(pygame.sprite.Sprite):
    file_name = 'Data/menu/closed.png'
    image = load_image(file_name, -25, -25)
    def __init__(self, obj):
        super().__init__(buttons_group)
        self.image = Closed.image
        self.rect = self.image.get_rect()
        self.obj = obj
        self.rect.right = obj.rect.right - 10
        self.rect.bottom = obj.rect.bottom -10

    def update(self, *args):
        pass

class Buttons_menu(pygame.sprite.Sprite):
    path = 'Data/menu/'
    images=[]
    for i in range(1, kol_levels+1):
        file_name = path + str(i) + '.jpg'
        images.append(load_image(file_name, -2, -2))

    @staticmethod
    def get_position(n):
        y = None
        kf=None
        if n<=5:
            kf = n
            y = 150
        elif n>5:
            kf = n-5
            y = 370
        x = 40*kf + 200*(kf-1)
        return x,y

    def __init__(self, screen, n):
        super().__init__(buttons_group)
        self.number = n
        self.image = Buttons_menu.images[n-1]
        self.rect = self.image.get_rect()
        x, y = Buttons_menu.get_position(n)
        self.rect.x = x
        self.rect.y = y
        self.button = myGUI.ImageButton(self.image, self.rect.width, self.rect.height)
        self.button.set_button(screen, self. rect.x, self.rect.y)
        self.reiting = Reiting(self, randint(0,5))
        self.closed = None
        if not level_dict[n].is_ready:
            self.closed = Closed(self)
        if self.number > 1 and get_reiting(self.number - 1, get_points_of_gamer_on_level(self.number - 1)) < 3:
            self.closed = Closed(self)
        self.data_result = Data_result(self)

    def update(self, *args):
        pass

def start_main_menu(screen):
    play_fone_music('Data/Sound/menu') # включаем фоновую музыку
    bg_group.empty()
    buttons_group.empty()
    Bg_menu()
    NameGame()
    global make_new_gamer
    make_new_gamer = MakeNewGamer(screen)
    global name_gamer
    name_gamer = NameGamer(screen)
    global del_gamer
    del_gamer = Del_gamer(screen)
    buttons = []
    for i in range(1,kol_levels+1):
        buttons.append(Buttons_menu(screen, i))
    select_level = get_command_from_user(screen)
    return select_level

def get_command_from_user(screen):
    select_level = None
    while select_level == None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                mydef.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for butt in buttons_group:
                    if isinstance(butt, Buttons_menu) and butt.button.check_click(event.pos):
                        select_level = butt.number
                        print(select_level)
                        if not level_dict[select_level].is_ready or butt.closed != None:
                            select_level = None
                name_gamer.check_click(event.pos)
                make_new_gamer.check_click(event.pos)
                del_gamer.check_click(event.pos)
            if make_new_gamer.is_input and event.type==pygame.KEYDOWN:
                make_new_gamer.eventing(event)
            if del_gamer.is_input and event.type == pygame.KEYDOWN:
                del_gamer.eventing(event)



        screen.fill((0,0,0))
        bg_group.update()
        bg_group.draw(screen)
        buttons_group.update()
        buttons_group.draw(screen)
        pygame.display.flip()


    result = select_level
    return result





