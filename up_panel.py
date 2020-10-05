import pygame
import public_vars
import myGUI
import mydef
import levels
import data_gamers
import glb
import menu

UP_PANEL = None

class AboutLevel(pygame.sprite.Sprite):
    font = pygame.font.Font('MagistralC.otf', 20)
    font.set_bold(True)
    shot_image = mydef.load_image('Data/Ammunition_Icon.png', -2, -2)
    armor_image = mydef.load_image('Data/Armor_Icon.png', -2, -2)
    def __init__(self):
        super().__init__(public_vars.labelsprites_group)
        self.image = pygame.Surface((900, 80))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.text = levels.get_name_level() + ' : ' + data_gamers.get_now_gamer() + ' : ' + str(glb.hero.points)
        self.label = myGUI.Text_label(self.text, self.font, (250, 100, 0), 50, 20, v=1)
        self.label.set_label(self.image, 0, 0)
        self.stars = myGUI.ImageButton(Stars.get_image_stars(), Stars.width, 20)
        self.stars.set_button(self.image, self.label.rect.right + 10, self.label.rect.y )
        self.img_shots = myGUI.ImageButton(self.shot_image, self.shot_image.get_width(), 30, v=1)
        self.img_shots.set_button(self.image, 0, 25)
        self.text_shots = str(glb.hero.gun.shots)
        self.txt_shots = myGUI.Text_label(self.text_shots, self.font, (250, 100, 0), 30, 20, v=1)
        self.txt_shots.set_label(self.image, 20, 25)
        self.img_armor = myGUI.ImageButton(self.armor_image, self.armor_image.get_width(), 30, v=1)
        self.img_armor.set_button(self.image, 0, 45)

        if glb.hero.protect != None:
            self.text_armor = str(glb.hero.protect.health)
        else:
            self.text_armor = '0'
        self.txt_armor = myGUI.Text_label(self.text_armor, self.font, (250, 100, 0), 50, 20, v=1)
        self.txt_armor.set_label(self.image, 28, 56)
        self.rect.x = 10
        self.rect.y = 10

        # self. = 'Результат: ' + str(glb.hero.points)
        #         # self.text = myGUI.Text_label(self.text_result, self.font, (250, 100, 0), 600, 50)
        #         # self.text.set_label(self.image, 0, 130)
        #         # self.image_reiting = self.images_reiting[levels.get_reiting(glb.num_level, glb.hero.points)]
        #         # x = (self.image.get_width() // 2) - (self.image_reiting.get_width() // 2)
        #         # self.image.blit(self.image_reiting, (x, 190))
    def update(self, *args):
        self.image.fill((0,0,0))
        self.text = levels.get_name_level() + ' : ' + data_gamers.get_now_gamer() + ' : ' + str(glb.hero.points)
        self.label = myGUI.Text_label(self.text, self.font, (250, 100, 0), self.label.get_widht(), 20, v=1)
        self.label.set_label(self.image, 0, 0)

        self.stars = myGUI.ImageButton(Stars.get_image_stars(), Stars.width, 20)
        self.stars.set_button(self.image, self.label.rect.right + 10, self.label.rect.y-5)

        self.img_shots = myGUI.ImageButton(self.shot_image, self.shot_image.get_width(), 30, v=1)
        self.img_shots.set_button(self.image, 0, 25)

        self.text_shots = str(glb.hero.gun.shots)
        self.txt_shots = myGUI.Text_label(self.text_shots, self.font, (250, 100, 0), 80, 20, v=1)
        self.txt_shots.set_label(self.image, 28, 28)

        self.img_armor = myGUI.ImageButton(self.armor_image, self.armor_image.get_width(), 30, v=1)
        self.img_armor.set_button(self.image, 0, 52)

        if glb.hero.protect !=None:
            self.text_armor = str(glb.hero.protect.health)
        else:
            self.text_armor = '0'
        self.txt_armor = myGUI.Text_label(self.text_armor, self.font, (250, 100, 0), 50, 20, v=1)
        self.txt_armor.set_label(self.image, 28, 56)

class Stars(menu.Reiting):
    path = 'Data/raiting/'
    images = []
    for i in range(6):
        file_name = path + str(i) + '.png'
        images.append(mydef.load_image(file_name, -10, -10))
    width = 0
    @staticmethod
    def get_image_stars():
        result = Stars.images[levels.get_reiting(glb.num_level, glb.hero.points)]
        Stars.width = result.get_width()
        return result




