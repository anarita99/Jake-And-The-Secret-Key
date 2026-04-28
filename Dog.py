import pygame
from Configs import Configs
from Bone import Bone
from Enemy import Enemy

# sounds
pygame.mixer.init()
snd_kill_enemy = pygame.mixer.Sound('sounds/kill_enemy_sound.wav')
snd_shoot = pygame.mixer.Sound('sounds/shoot_sound.wav')
snd_hurt = pygame.mixer.Sound('sounds/hurt_sound.wav')


class Dog:
    STANDING = 0
    WALKING = 1
    JUMPING = 2
    FALLING = 3

    def __init__(self):
        self.__x = 50
        self.__y = 358
        self.__img = Configs.IMG_DOG_STANDING
        self.__lives = 3
        self.__state = Dog.STANDING
        self.__sprite_position = 0
        self.__count_frames = 0
        self.__tot_jump_frames = 0
        self.__bones = []
        self.__cool_down_count = 0
        self.__total_immortal_frames = 0

    def get_xy(self):
        return self.__x, self.__y

    def get_img(self):
        return self.__img

    def draw_me(self):
        if not self.is_immortal() or (self.is_immortal() and self.__total_immortal_frames % 5 == 0):
            if self.is_immortal():
                pygame.display.get_surface().blit(pygame.image.load('imgs/halo.png'), (self.__x, self.__y - 25))

            pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def change_state(self, state):
        self.__state = state
        self.__count_frames = 0
        self.__sprite_position = 0

    def shoot(self, is_shoot_key_pressed):
        self.cooldown()

        if is_shoot_key_pressed and self.can_shoot():
            self.start_shoot()
            snd_shoot.play()
            bone = Bone(self.__x + 30, self.__y + 10)
            self.__bones.append(bone)

    def get_bones(self):
        return self.__bones

    def manage_bones(self, enemy_group):
        for bone in self.__bones:
            bone.draw_bone()
            bone.move()
            if bone.off_screen():
                self.__bones.remove(bone)
                continue

            for enemy in enemy_group:
                if bone.collides(enemy):
                    snd_kill_enemy.play()
                    enemy_group.remove(enemy)
                    self.__bones.remove(bone)

                    for x in range(1):
                        enemy_group.append(Enemy())

    def hurt_boss(self, the_boss):
        for bone in self.__bones:
            bone.draw_bone()
            bone.move()
            if bone.off_screen():
                self.__bones.remove(bone)
            if bone.collides(the_boss):
                the_boss.lose_life()
                self.__bones.remove(bone)

    def start_shoot(self):
        self.__cool_down_count = 20

    def can_shoot(self):
        return self.__cool_down_count == 0

    def cooldown(self):
        if self.__cool_down_count == 0:
            return

        self.__cool_down_count -= 1

    def move(self, move_left, move_right, jump):
        if self.__total_immortal_frames > 0:
            self.__total_immortal_frames -= 1

        if self.__total_immortal_frames > 0:
            self.__total_immortal_frames -= 1
        # self.__printState()

        if self.__state != Dog.JUMPING and self.__state != Dog.FALLING:
            if jump:
                self.change_state(Dog.JUMPING)
            else:
                if (move_left or move_right) and self.__state != Dog.WALKING:
                    self.change_state(Dog.WALKING)
                elif not move_left and not move_right:
                    self.change_state(Dog.STANDING)

        # esquerda
        if move_left and self.__x >= 20:
            self.__x -= 2
        # direita
        elif move_right and self.__x <= 900 - self.__img.get_width():
            self.__x += 2

    def update_jump(self):
        if self.__state != Dog.JUMPING and self.__state != Dog.FALLING:
            return

        self.__tot_jump_frames += 1
        if self.__state == Dog.JUMPING:
            self.__y -= 3
        elif self.__state == Dog.FALLING:
            self.__y += 3

        if self.__tot_jump_frames > 30:
            self.__tot_jump_frames = 0
            if self.__state == Dog.JUMPING:
                self.change_state(Dog.FALLING)
            else:
                self.change_state(Dog.STANDING)

    def toggle_sprite(self):
        self.__count_frames += 1
        if self.__state == Dog.WALKING and self.__count_frames % 7 != 0:
            return
        elif self.__state == Dog.STANDING:
            self.__img = Configs.IMG_DOG_STANDING
            return
        elif self.__state == Dog.JUMPING and self.__count_frames % 5 != 0:
            return
        elif self.__state == Dog.FALLING and self.__count_frames % 5 != 0:
            return

        self.__count_frames = 0
        self.__sprite_position += 1
        if self.__state == Dog.WALKING:
            self.__img = Configs.SPRITE_DOG_WALK[self.__sprite_position]
            if self.__sprite_position == 7:
                self.__sprite_position = -1
        # saltar
        elif self.__state == Dog.JUMPING:
            self.__img = Configs.SPRITE_DOG_JUMP[self.__sprite_position]
            if self.__sprite_position == 1:
                self.__sprite_position = -1
        # cair
        elif self.__state == Dog.FALLING:
            self.__img = Configs.SPRITE_DOG_FALL[self.__sprite_position]
            if self.__sprite_position == 5:
                self.__sprite_position = -1

    def get_bounds(self):
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def collides(self, who):
        return self.get_bounds().colliderect(who.get_bounds())

    def lose_life(self):
        if self.is_immortal():
            return

        self.__lives -= 1
        snd_hurt.play()
        if self.__lives == 0:
            self.__lives = 0

    def go_temp_immortal(self):
        self.__total_immortal_frames = 300

    def is_immortal(self):
        return self.__total_immortal_frames > 0

    def is_not_immortal(self):
        return self.__total_immortal_frames <= 0

    def get_lives(self):
        return self.__lives

    def is_dead(self):
        return self.__lives == 0

    def restart_lives(self):
        self.__lives = 3
