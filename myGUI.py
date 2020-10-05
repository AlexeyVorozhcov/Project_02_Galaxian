import pygame

def to_make_surf_from_text(text, font, color_text, color_fon=None):
    text_p = font.render(text, 0, color_text, color_fon)
    text_w, text_h = text_p.get_width(), text_p.get_height()
    surf = pygame.Surface((text_w, text_h))
    surf.fill((0,0,0))
    surf.set_colorkey((0, 0, 0))
    surf.blit(text_p, (0,0))
    return surf

class Text_label():
    def __init__(self, text, font, color_text, w, h, border=0, color_border=(0,0,0), color_feel=(0,0,0), v=2):
        self.text = text
        self.font = font
        self.color_text = color_text
        self.border = border
        self.color_border = color_border
        self.color_feel = color_feel
        self.image = to_make_surf_from_text(self.text, self.font, self.color_text)
        self.label = pygame.Surface((w, h))
        self.rect = self.label.get_rect()
        self.w = w
        self.h = h
        if border!=0:
            self.label.fill(self.color_feel)
            pygame.draw.rect(self.label, self.color_border, (0,0, w, h), self.border)
        else:
            self.label.set_colorkey((0,0,0))
        text_rect = self.image.get_rect()
        if v==2: text_rect.center = self.label.get_rect().center
        if v==1: text_rect.left = self.label.get_rect().left
        self.label.blit(self.image, text_rect)

    def get_widht(self):
        return self.image.get_width()

    def set_label(self, surf, x, y):
        surf.blit(self.label, (x,y))
        self.rect = self.label.get_rect()
        self.rect = self.rect.move(x,y)




class TextButton():
    def __init__(self, text, font, color_text, w, h, border, color_border, color_feel, v=2):
        self.text = text
        self.font = font
        self.color_text = color_text
        self.border = border
        self.color_border = color_border
        self.color_feel = color_feel
        self.image = to_make_surf_from_text(self.text, self.font, self.color_text)
        self.button = pygame.Surface((w, h))
        self.rect = self.button.get_rect()
        self.w = self.image.get_width()
        self.h = h
        if border!=0:
            self.button.fill(self.color_feel)
            pygame.draw.rect(self.button, self.color_border, (0,0, w, h), self.border)
        else:
            self.button.set_colorkey((0,0,0))
        text_rect = self.image.get_rect()
        if v == 2: text_rect.center = self.button.get_rect().center
        if v == 1: text_rect.left = self.button.get_rect().left
        self.button.blit(self.image, text_rect)

    def set_button(self, surf, x, y):
        surf.blit(self.button, (x,y))
        self.rect = self.button.get_rect()
        self.rect = self.rect.move(x,y)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

class ImageButton():
    def __init__(self, image, w, h, v=2):
        self.image = image
        self.button = pygame.Surface((w, h))
        self.button.set_colorkey((0,0,0))
        self.rect = self.button.get_rect()
        image_rect = self.image.get_rect()
        if v==2: image_rect.center = self.button.get_rect().center
        if v == 1: image_rect.x = self.button.get_rect().x
        self.button.blit(self.image, image_rect)
        self.w = w
        self.h = h

    def set_button(self, surf, x, y):
        surf.blit(self.button, (x,y))
        self.rect = self.button.get_rect()
        self.rect = self.rect.move(x,y)
        #print (self.rect)

    def get_widht(self):
        return self.image.get_width()

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False