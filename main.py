import math

import pygame
import random

pygame.init()
screen_width = 500
screen_height = 600

pygame.display.set_caption("Space invader")
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.image.load("v907-aum-41.jpg")

# Main player
player_img = pygame.image.load("image/space-shuttle.png")
player_X = 230
player_Y = 530


def draw_player(player_X, player_Y):
    screen.blit(player_img, (player_X, player_Y))


# bullet firing
bullet_width = 0
bullet_height = player_Y
bullet_speed = 0.5
bullet_img = pygame.image.load("bullet.png")
bullet_status = "ready"


def bullet_firing(x, y):
    global bullet_status
    screen.blit(bullet_img, (x, y))


# Alien
alien_num = 8
alien_img = []
alien_width = []
alien_height = []
alien_speed = []
for i in range(alien_num):
    alien_img.append(pygame.image.load("image/rocket.png"))
    alien_width.append(random.randint(0, 450))
    alien_height.append(random.randint(-100, 0))
    alien_speed.append(0.1)


def draw_alien(alien_w, alien_h, i):
    screen.blit(alien_img[i], (alien_w, alien_h))


# ALien bullet firing
alien_bullet_width = []
alien_bullet_height = []
alien_bullet_speed = []
alien_bullet_img = []
alien_bullet_status = []
for i in range(alien_num):
    alien_bullet_width.append(0)
    alien_bullet_height.append(alien_height[i])
    alien_bullet_speed.append(0.3)
    alien_bullet_img.append(pygame.image.load("enemyBullet.png"))
    alien_bullet_status.append("False")


def alien_bullet_firing(alien_x, alien_y, i):
    screen.blit(alien_bullet_img[i], (alien_x, alien_y))


def is_collision(alien_x, alien_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(alien_x - bullet_x, 2) + math.pow(alien_y - bullet_y, 2))
    if distance < 40:
        return True
    else:
        return False


run = True
while run:
    guess = random.randint(0, 200)
    pygame.display.update()
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if player_X >= 440:
                    player_X = 450
                else:
                    player_X += 20
            if event.key == pygame.K_LEFT:
                if player_X <= 0:
                    player_X = 0
                else:
                    player_X -= 20
            if event.key == pygame.K_SPACE:
                if bullet_status == "ready":
                    bullet_status = "fire"
                    bullet_width = player_X + 20

    draw_player(player_X, player_Y)
    if bullet_status == "fire":
        if bullet_height < 0:
            bullet_status = "ready"
            bullet_height = player_Y
        bullet_firing(bullet_width, bullet_height)
        bullet_height -= bullet_speed

    for i in range(alien_num):

        if guess == 3:
            alien_bullet_status[i] = "True"
        if alien_bullet_status[i] == "True":
            alien_bullet_height[i] += alien_bullet_speed[i]
            alien_bullet_firing(alien_width[i] + 20, alien_bullet_height[i] + 60, i)

        alien_height[i] += alien_speed[i]
        if alien_height[i]>590:
            alien_height[i]=random.randint(-100, 0)
        draw_alien(alien_width[i], alien_height[i], i)

        if is_collision(alien_width[i], alien_height[i], bullet_width, bullet_height):
            print("hello")
            alien_width[i] = random.randint(0, 450)
            alien_height[i] = random.randint(-100, 0)
