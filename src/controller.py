import pygame


# Created by Emanuel Ramirez Alsina on 03/23/2020

class Getkey:
    def __init__(self, game):
        self.game = game
        self.key_map = {
            'UP'    :   pygame.K_w,
            'DOWN'  :   pygame.K_s,
            'LEFT'  :   pygame.K_a,
            'RIGHT' :   pygame.K_d
        }
