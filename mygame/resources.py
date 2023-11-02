import pygame
import os

pygame.init()
pygame.mixer.init()

# Wymiary okna
screen_info = pygame.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h

# Tworzenie okna
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Wymiary planszy i płytki
BOARD_WIDTH = 500
BOARD_HEIGHT = 600
TILE_WIDTH = 80
TILE_HEIGHT = 100

# Kolory
BACKGROUND = (111, 155, 114)
YELLOW = (216, 160, 71)
BROWN = (182, 101, 69)
INDIGO = (141, 144, 202)
RED = (185, 59, 24)
WHITE = (255, 249, 227)

# Wczytywanie grafik
path = os.path.join(os.pardir, 'images')
file_names = sorted(os.listdir(path))
IMAGES = {}
for file_name in file_names:
    IMAGES[file_name[:-4].upper()] = pygame.image.load(os.path.join(path, file_name)).convert_alpha()

# Wczytywanie efektów dźwiękowych
path = os.path.join(os.pardir, 'sounds')
match_sound = pygame.mixer.Sound(os.path.join(path, 'match_sound.wav'))
victory_music = pygame.mixer.Sound(os.path.join(path, 'victory_music.wav'))
game_over_music = pygame.mixer.Sound(os.path.join(path, 'game_over_music.wav'))
victory_music_played = False
game_over_music_played = False

# Zdarzenie animacji
ANIMATION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_EVENT, 6)







