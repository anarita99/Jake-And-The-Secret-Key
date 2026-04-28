import pygame
from Configs import Configs

class Bone:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Configs.IMG_BONE

    def move(self):
        self.__x += 15

    def draw_bone(self):
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def off_screen(self):
        return not(self.__x <= 889)

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def collides(self, who):
        return self.get_bounds().colliderect(who.get_bounds())
