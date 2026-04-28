import pygame
from Configs import Configs
from random import *

class Enemy:
    RUN = 0
    def __init__(self):
        self.__x = randint(Configs.SCREEN_W, 2000)
        self.__y = 368
        self.__img = Configs.SPRITE_ENEMY_RUN[0]
        self.__sprite_position = 0
        self.__state = 0
        self.__count_frames = 0

    def get_xy(self):
        return self.__x, self.__y

    def get_img(self):
        return self.__img

    def update_sprite(self):
        self.__count_frames += 1

        if self.__state == Enemy.RUN and self.__count_frames % 10 != 0:
            return

        self.__count_frames = 0
        self.__sprite_position += 1

        if self.__state == Enemy.RUN:
            self.__img = Configs.SPRITE_ENEMY_RUN[self.__sprite_position]
            if self.__sprite_position == 11:
                self.__sprite_position = -1

    def run(self):
        self.__x -= 3
        if self.__x < 0:
            self.__x = pygame.display.get_surface().get_width() + randint(0, 180)

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def collides(self, who):
        return self.get_bounds().colliderect(who.get_bounds())