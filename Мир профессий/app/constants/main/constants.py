import pygame
import os
import sys
pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

GAME_NAME = "Мир профессий"
SCREEN_SIZE = (640, 480)
FONT = pygame.font.Font(resource_path("app/assets/font/Milk(RUS BY LYAJKA) Regular.ttf"), 24)
SMALL_FONT = pygame.font.Font(resource_path("app/assets/font/Milk(RUS BY LYAJKA) Regular.ttf"), 16)
SMALLER_FONT = pygame.font.Font(resource_path("app/assets/font/Milk(RUS BY LYAJKA) Regular.ttf"), 10)
GITHUB_LINK = "https://github.com/Weoge/Quiz-Game"
