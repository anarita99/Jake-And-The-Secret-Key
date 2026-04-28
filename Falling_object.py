import pygame
from random import *
from Configs import *

class Falling_object:
    def __init__(self):
        self.__img = None
        self.__x = 0
        self.__y = 0
        self.__is_skull = False
        self.reposition()

    def reposition(self):
        self.__is_skull = choice((True, False))
        if self.__is_skull:
            self.__img = choice(Configs.IMGS_SKULL)
        else:
            self.__img = choice(Configs.IMGS_COINS)

        self.__x = randint(Configs.SCREEN_W, Configs.SCREEN_W + 200)
        self.__y = randint(-50, -self.__img.get_height())

    def is_skull(self):
        return self.__is_skull

    def get_xy(self):
        return self.__x, self.__y

    def get_img(self):
        return self.__img

    def fall(self):
        if self.__y < 408 - self.__img.get_height():
            self.__y += 3
            self.__x -= 2
        elif self.__y >= 408 - self.__img.get_height():
            self.__x -= 2

        if self.__x <= 0 - self.__img.get_width():
            self.reposition()

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())
