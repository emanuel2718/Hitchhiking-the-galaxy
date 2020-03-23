import pygame
import traceback

import main

# Created by Emanuel Ramirez Alsina on 03/22/2020

if __name__ == '__main__':
    try:
        game = main.Game()
        game.main()
    except:
        traceback.print_exc()
        pygame.quit()




