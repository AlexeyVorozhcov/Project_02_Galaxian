import pygame
import mydef
import random

try:
    pygame.init()
except Exception:
    print("Ошибка со звуком main_sounds_init. Нажмите Enter...")
    input()

soundfiles_01 = mydef.get_list_files('Data/Sound/01', '.wav')
soundfiles_02 = mydef.get_list_files('Data/Sound/02', '.wav')
soundfiles_03 = mydef.get_list_files('Data/Sound/03', '.wav')
fonfiles = mydef.get_list_files('Data/Sound/fon', '.mp3')
bonusfiles = mydef.get_list_files('Data/Sound/bonus', '.wav')
bonusfiles_saturn = mydef.get_list_files('Data/Sound/bonus_saturn', '.wav')
sounds_01 = []
sounds_02 = []
sounds_03 = []
sounds_b = []
sounds_b_s = []


for i in soundfiles_01:
    namefile = 'Data/Sound/01/' + i
    sounds_01.append(pygame.mixer.Sound(namefile))
for i in soundfiles_02:
    namefile = 'Data/Sound/02/' + i
    sounds_02.append(pygame.mixer.Sound(namefile))
for i in soundfiles_03:
    namefile = 'Data/Sound/03/' + i
    sounds_03.append(pygame.mixer.Sound(namefile))
for i in bonusfiles:
    namefile = 'Data/Sound/bonus/' + i
    sounds_b.append(pygame.mixer.Sound(namefile))
for i in bonusfiles_saturn:
    namefile = 'Data/Sound/bonus_saturn/' + i
    sounds_b_s.append(pygame.mixer.Sound(namefile))

def play_sound(type):
    try:
        if type==1:
            random.choice(sounds_01).play()
        if type==2:
            random.choice(sounds_02).play()
        if type==3:
            random.choice(sounds_03).play()
        if type==4:
            random.choice(sounds_b).play()
        if type==5:
            random.choice(sounds_b_s).play()
    except Exception:
        print("Ошибка со звуком main_play_sound. Нажмите Enter...")
        input()


def sound_play(sound):
    sound.play()

def play_fone_music():
    try:
        namefile = 'Data/Sound/fon/' + random.choice(fonfiles)
        pygame.mixer.music.load(namefile)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception:
        print("Ошибка со звуком main_play_fone_music. Нажмите Enter...")
        input()

def stop_fone_music():
    pygame.mixer.music.pause()
