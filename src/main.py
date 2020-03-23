#!/usr/bin/bash

import pygame

import config
import controller as control

# Created by Emanuel Ramirez Alsina on 03/22/2020

class Game:
    '''Main game driver.'''

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game Engine')

        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)

        # Background
        self.background = pygame.image.load('../assets/images/background.jpg')
        #self.background_height = background.get_rect().height

        # TODO: Change the player to it's own class.
        # Player spawn
        self.playerSprite = pygame.image.load('../assets/images/spaceship_normal.png')
        self.player_x = int(config.SCREEN_WIDTH / 2) - 30
        self.player_y = int(600 / 1.25)

        # Will update the movement of the player
        self.delta_player_x = 0
        self.delta_player_y = 0


    # Main loop of the game.
    def main(self):
        self.running = True
        while self.running:
            self.screen.fill(config.BLUE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                pygame.display.update()
