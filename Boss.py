# GATO
import pygame
from Dog import Dog
from Configs import Configs
from random import *
from Direction import *
from Candy import *
from Timer import *

# sounds
pygame.mixer.init()
snd_shoot_candy = pygame.mixer.Sound('sounds/shoot_candy_sound.wav')
snd_shoot_candy.set_volume(0.04)

class Boss:

    def __init__(self):
        self.__img = Configs.SPRITE_CAT_WALK[0]
        self.__x = randint(440, 800)
        self.__y = randint(345, 360)
        self.__lives = 5
        self.__count_frames = 0
        self.__sprite_position = 0
        self.__candies = []
        self.__cool_down_count = 0
        self.__direction_horizontal = Direction.LEFT
        self.__direction_vertical = Direction.LEFT
        self.__shoot_timer = Timer(2)

    def get_xy(self):
        return self.__x, self.__y

    def walk_sprite(self):
        self.__count_frames += 1
        if self.__count_frames % 7 != 0:
            return

        self.__count_frames = 0
        self.__sprite_position += 1
        self.__img = Configs.SPRITE_CAT_WALK[self.__sprite_position]
        if self.__sprite_position == 2:
            self.__sprite_position = -1

    def draw_me(self):
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def handle_candies(self, dog):
        if self.__shoot_timer.hasEnded():
            self.__shoot_timer.reset()

            candy = Candy(self.__x - self.__img.get_width(), self.__y + 20)
            self.__candies.append(candy)

        for candy in self.__candies:
            candy.move()
            snd_shoot_candy.play()
            candy.draw_candy()

            if candy.off_screen():
                self.__candies.remove(candy)
                return

            if dog.collides(candy):
                self.__candies.remove(candy)
                dog.lose_life()



    def move(self):
        """x 440
            Configs.SCREEN_W - self.__img.get_width()

            y
              360
              160
        """
        toggleDirection = False

        if self.__x < 440:  # left
            self.__x = 440
            toggleDirection = True
        elif self.__x > Configs.SCREEN_W - self.__img.get_width():  # right
            self.__x = Configs.SCREEN_W - self.__img.get_width()
            toggleDirection = True
        elif self.__y < 50:  # top
            self.__y = 50
            toggleDirection = True
        elif self.__y > 360:  # bot
            self.__y = 360
            toggleDirection = True

        if toggleDirection:
            self.__direction_horizontal = choice((Direction.LEFT, Direction.RIGHT, Direction.NONE))
            self.__direction_vertical = choice((Direction.TOP, Direction.BOTTOM, Direction.NONE))

            #garantir que não ficam as duas com direção NONE
            if self.__direction_horizontal == Direction.NONE and self.__direction_vertical == Direction.NONE:
                self.__direction_horizontal = choice((Direction.LEFT, Direction.RIGHT))


        if self.__direction_horizontal == Direction.LEFT:
            self.__x -= randint(1, 3)
        elif self.__direction_horizontal == Direction.RIGHT:
            self.__x += randint(1, 3)

        if self.__direction_vertical == Direction.TOP:
            self.__y -= randint(1, 3)
        elif self.__direction_vertical == Direction.BOTTOM:
            self.__y += randint(1, 3)

    def get_lives(self):
        return self.__lives


    def lose_life(self):
        self.__lives -= 1

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def collides(self, who):
        return self.get_bounds().colliderect(who.get_bounds())


    def is_dead(self):
        return self.__lives == 0