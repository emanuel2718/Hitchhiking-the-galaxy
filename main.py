#!/usr/bin/bash

import pygame

# Movement Keys
UP =    pygame.K_w
DOWN =  pygame.K_s
LEFT =  pygame.K_a
RIGHT = pygame.K_d

# RGB values
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('SpacEnemy')


# Background
background = pygame.image.load('images/background.jpg')
background_height = background.get_rect().height

# Player
playerSprite = pygame.image.load('images/spaceship_normal.png')
player_x = int(SCREEN_WIDTH / 2) - 30
player_y = int(600 / 1.25)

# Start the game
pygame.init()

def player(x, y):
    screen.blit(background, (0, 0))
    screen.blit(playerSprite, (player_x, player_y))



running = True
while running:
    screen.fill(BLACK)
    #player_y -= 1
    #player_x -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == UP:
                player_y -= 6
            if event.key == DOWN:
                player_y += 6
            if event.key == LEFT:
                player_x -= 6
            if event.key == RIGHT:
                player_x += 6

    player(player_x, player_y)
    pygame.display.update()

