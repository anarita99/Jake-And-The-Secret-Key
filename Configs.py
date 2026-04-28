import pygame

class Configs:
    SCREEN_W = 889
    SCREEN_H = 500

    # IMG BG
    IMG_BG = pygame.image.load("imgs/bg/bg1.png")
    IMG_START_GAME = pygame.image.load('imgs/bg/bg_start_game.jpg')
    IMG_GAME_OVER = pygame.image.load('imgs/bg/bg_game_over.jpg')
    IMG_BG_FINAL_BOSS = pygame.image.load('imgs/bg/bg_final_boss.png')
    IMG_THE_END = pygame.image.load('imgs/bg/bg_the_end.png')

    IMG_DOG_STANDING = pygame.image.load('imgs/standing/standing_dog.png')

    SPRITE_DOG_WALK = (
        pygame.image.load('imgs/walk_dog/Walk_dog(1).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(2).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(3).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(4).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(5).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(6).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(7).png'),
        pygame.image.load('imgs/walk_dog/Walk_dog(8).png'),

    )

    SPRITE_DOG_JUMP = (
        pygame.image.load('imgs/jump_dog/jump(1).png'),
        pygame.image.load('imgs/jump_dog/jump(2).png'),

    )

    SPRITE_DOG_FALL = (
        pygame.image.load('imgs/jump_dog/jump(3).png'),
        pygame.image.load('imgs/jump_dog/jump(4).png'),
        pygame.image.load('imgs/jump_dog/jump(5).png'),
        pygame.image.load('imgs/jump_dog/jump(6).png'),
        pygame.image.load('imgs/jump_dog/jump(7).png'),
        pygame.image.load('imgs/jump_dog/jump(8).png'),
    )

    SPRITE_ENEMY_RUN = (
        pygame.image.load('imgs/run_enemy/Run (1).png'),
        pygame.image.load('imgs/run_enemy/Run (2).png'),
        pygame.image.load('imgs/run_enemy/Run (3).png'),
        pygame.image.load('imgs/run_enemy/Run (4).png'),
        pygame.image.load('imgs/run_enemy/Run (5).png'),
        pygame.image.load('imgs/run_enemy/Run (6).png'),
        pygame.image.load('imgs/run_enemy/Run (7).png'),
        pygame.image.load('imgs/run_enemy/Run (8).png'),
        pygame.image.load('imgs/run_enemy/Run (9).png'),
        pygame.image.load('imgs/run_enemy/Run (10).png'),
        pygame.image.load('imgs/run_enemy/Run (11).png'),
        pygame.image.load('imgs/run_enemy/Run (12).png'),
    )

    IMG_LIFE = pygame.image.load('imgs/life.png')

    IMGS_COINS = (
        pygame.image.load('imgs/coins/coin (1).png'),
        pygame.image.load('imgs/coins/coin (2).png'),
        pygame.image.load('imgs/coins/coin (3).png'),
        pygame.image.load('imgs/coins/coin (4).png')
    )

    IMGS_CANDY = (
        pygame.image.load('imgs/candy/candy (1).png'),
        pygame.image.load('imgs/candy/candy (2).png'),
        pygame.image.load('imgs/candy/candy (3).png'),
        pygame.image.load('imgs/candy/candy (4).png')
    )

    IMG_BONE = pygame.image.load('imgs/bone.png')

    IMG_OBSTACLE = pygame.image.load('imgs/obstacle.png')

    IMGS_SKULL = (
        pygame.image.load('imgs/skull/skull (1).png'),
        pygame.image.load('imgs/skull/skull (2).png')
    )

    SPRITE_CAT_WALK = (
        pygame.image.load('imgs/walk_cat/Walk_cat(1).png'),
        pygame.image.load('imgs/walk_cat/Walk_cat(2).png'),
        pygame.image.load('imgs/walk_cat/Walk_cat(3).png'),
    )

    IMG_CAT_STANDING = pygame.image.load('imgs/standing/standing_kitty.png')

    IMG_KEY = pygame.image.load('imgs/key.png')