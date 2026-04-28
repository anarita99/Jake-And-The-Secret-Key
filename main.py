import sys
import pygame
from Dog import Dog
from Configs import Configs
from Enemy import Enemy
from Falling_object import *
from Secret_key import *
from Boss import *

# game screen
pygame.init()
pygame.display.set_caption('Jake & The Secret Key')
screen = pygame.display.set_mode((Configs.SCREEN_W, Configs.SCREEN_H))

# icon
icon = pygame.image.load('imgs/icon.png')
pygame.display.set_icon(icon)

# clock
clock = pygame.time.Clock()

# fonts
pygame.font.init()
font1 = pygame.font.Font('fonts/SpaceMono-Bold.ttf', 15)
font2 = pygame.font.Font('fonts/SpaceMono-Bold.ttf', 40)
font3 = pygame.font.Font('fonts/SpaceMono-Bold.ttf', 60)

# sounds
pygame.mixer.init()
bg_music = pygame.mixer.Sound('sounds/bg_sound.wav')
boss_bg_music = pygame.mixer.Sound('sounds/boss_bg_sound.wav')
snd_win = pygame.mixer.Sound('sounds/win_sound.wav')
snd_game_over = pygame.mixer.Sound('sounds/game_over_sound.wav')
snd_catch_key = pygame.mixer.Sound('sounds/key_sound.wav')
snd_hurt = pygame.mixer.Sound('sounds/hurt_sound.wav')
snd_catch_coin = pygame.mixer.Sound('sounds/coin_sound.wav')

# characters and objects
dog = Dog()
boss = Boss()

secret_key = Secret_key()

enemies = []
objects = []


def reset_game():
    global enemies, objects, dog, boss, boss_bg_music

    boss_bg_music.stop()

    enemies.clear()
    objects.clear()

    for x in range(3):
        enemies.append(Enemy())

    for x in range(3):
        objects.append(Falling_object())

    # dog and boss reset
    dog = Dog()
    boss = Boss()
    game()


def start_game():
    global screen, clock, font2

    while True:
        clock.tick(60)
        screen.blit(Configs.IMG_START_GAME, (0, 0))
        text_start = font2.render("Press ENTER to START GAME", True, 'black')
        screen.blit(text_start, (50, 430))

        # to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # to start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        pygame.display.update()


def game():
    bg_music.play(loops=-1)
    global screen, clock, font1, dog, enemies, objects, secret_key

    screen_pos = 0
    running = True
    total_coins = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # background + text
        screen.blit(Configs.IMG_BG, (screen_pos, 0))
        screen.blit(Configs.IMG_BG, (Configs.SCREEN_W + screen_pos, 0))

        text = font1.render('Catch coins and kill the enemies till you find the secret key!', True, 'black')
        text2 = font1.render('Press SPACE to shoot', True, 'black')
        screen.blit(text, (50, 460))
        screen.blit(text2, (380, 23))

        if screen_pos == -Configs.SCREEN_W:
            screen_pos = 0
        screen_pos -= 1

        if dog.is_dead():
            snd_game_over.play()
            game_over()

        # lives and coins
        text = font1.render("Lives", True, 'black')
        screen.blit(text, (10, 23))

        for x in range(dog.get_lives()):
            screen.blit(Configs.IMG_LIFE, (30 * x + 60, 18))

        coins = font1.render(f"Coins: {total_coins} ", True, 'black')
        screen.blit(coins, (780, 23))

        # dog
        keys = pygame.key.get_pressed()
        dog.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP])
        dog.update_jump()
        dog.toggle_sprite()
        dog.draw_me()

        # shoot bone
        dog.shoot(keys[pygame.K_SPACE])
        dog.manage_bones(enemies)

        # enemies
        for enemy in enemies:
            enemy.update_sprite()
            enemy.run()

            if dog.is_not_immortal() and dog.collides(enemy):
                dog.lose_life()
                snd_hurt.play()
                dog.go_temp_immortal()

            screen.blit(enemy.get_img(), enemy.get_xy())

        # catch coins
        for object in objects:
            if dog.collides(object):
                if object.is_skull():
                    dog.lose_life()
                else:
                    snd_catch_coin.play()
                    total_coins += 1

                object.reposition()

            object.fall()
            screen.blit(object.get_img(), object.get_xy())

        if total_coins >= 10:
            secret_key.draw_key()
            if dog.collides(secret_key):
                snd_catch_key.play()
                game_final_boss()

        clock.tick(60)
        pygame.display.update()


def game_final_boss():
    global screen, clock, font1, dog, boss, bg_music

    bg_music.stop()
    boss_bg_music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(Configs.IMG_BG_FINAL_BOSS, (0, 0))
        text3 = font1.render('Kill the final boss to win!', True, '#2a6e1b', 'grey')
        screen.blit(text3, (50, 460))

        if dog.is_dead():
            snd_game_over.play()
            game_over()
            continue

        # lives and coins
        text_lives_dog = font1.render("Dog ", True, 'black')
        screen.blit(text_lives_dog, (10, 23))

        text_lives_cat = font1.render("Cat ", True, 'black')
        screen.blit(text_lives_cat, (850, 23))

        for x in range(dog.get_lives()):
            screen.blit(Configs.IMG_LIFE, (30 * x + 50, 18))

        for x in range(boss.get_lives()):
            screen.blit(Configs.IMG_LIFE, (30 * x + 695, 18))

        # dog
        keys = pygame.key.get_pressed()
        dog.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP])
        dog.update_jump()
        dog.toggle_sprite()
        dog.draw_me()

        # shoot bone
        dog.shoot(keys[pygame.K_SPACE])
        dog.hurt_boss(boss)
        if dog.collides(boss):
            dog.lose_life()

        boss.move()
        boss.walk_sprite()
        boss.draw_me()

        boss.handle_candies(dog)

        if boss.is_dead():
            boss_bg_music.stop()
            snd_win.play()
            you_win()

        clock.tick(60)
        pygame.display.update()


def game_over():
    while True:
        if dog.is_dead():
            screen.blit(Configs.IMG_GAME_OVER, (0, 0))
            text_game_over = font2.render("You died! Press R to restart", True, 'black')
            screen.blit(text_game_over, (50, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

        clock.tick(60)
        pygame.display.update()


def you_win():
    while True:
        if boss.is_dead():
            screen.blit(Configs.IMG_THE_END, (0, 0))
            text_you_win = font3.render("You Win!", True, 'black')
            text_rect = text_you_win.get_rect(center=(Configs.SCREEN_W / 2, Configs.SCREEN_H / 2))
            screen.blit(text_you_win, text_rect)
            text_thanks = font2.render("Thanks for playing!", True, 'white')
            screen.blit(text_thanks, (50, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()





# ---------------------------

start_game()
reset_game()
game()
game_final_boss()
