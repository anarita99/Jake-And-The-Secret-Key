import pygame
from Configs import *


class Secret_key:
    def __init__(self):
        self.__img = Configs.IMG_KEY
        self.__x = Configs.SCREEN_W / 3
        self.__y = 358 - self.__img.get_height()

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def draw_key(self):
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))
