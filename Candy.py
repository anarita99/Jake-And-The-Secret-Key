import pygame
from Configs import Configs
from random import *


class Candy:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = choice(Configs.IMGS_CANDY)

    def move(self):
        if self.__y >= 345:
            self.__x -= 15
        else:
            self.__x -= 10
            self.__y += 10

    def draw_candy(self):
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def off_screen(self):
        return not(self.__x >= 0)
