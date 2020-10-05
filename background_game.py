from public_vars import *
from logic_game import *
import user_control

class Background():
    def __init__(self, image, posx=0, speed=100):
        self.image = image
        self.w = self.image.get_width()
        self.posx = posx
        self.speed = speed
        self.time = pygame.time.get_ticks()
        self.abroad = WIDTH_GAMEBOARD - self.w
        self.is_shaking = False
        self.time_shaking = pygame.time.get_ticks()
        self.counter_shaking =0
        self.traversed = 0

    def draw_(self, screen):
        if self.is_shaking and not mydef.check_timer(self.time_shaking, 1000) :
            if self.counter_shaking>=0 and self.counter_shaking<=3:
                self.posx +=3
            if self.counter_shaking >= 4 and self.counter_shaking <= 7:
                self.posx -=3
            if self.counter_shaking ==7:
                self.counter_shaking = 0
            self.counter_shaking +=1
        else:
            self.is_shaking = False
            self.counter_shaking =0
            if mydef.check_timer(self.time, self.speed):
                self.posx -= 1
                self.time = pygame.time.get_ticks()
                self.traversed +=1
                #Level.make_object(Background.traversed)
                #print (Background.traversed)
                make_opponent(self.traversed)
                if check_level_complete():
                    print("LEVEL COMPLETE")
                    user_control.Level_comlete.level_comlpete()
        screen.blit(self.image, (self.posx, 0))
        if self.posx <= self.abroad:
            screen.blit(self.image, (self.posx + self.w   , 0))
        if abs(self.posx) >= self.w:
            self.posx = 0