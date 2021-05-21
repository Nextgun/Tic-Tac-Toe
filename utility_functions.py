#   This module contains Utility Functions that will be used regularly 
#   of semi regularly.
# 
#   Author: Hector M
#-------------------------------------------------------------

import pygame # import pygame
pygame.init() # initialize pygame

# Function that checks if the game is running; if not running, close game/app.
def check_if_running(event, running_test):
        # did the user click the window close button? if so, stop the loop
        if event.type == pygame.QUIT:
            running_test = False
            return running_test
        # did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # was it the Escape Key? if so, stop the loop
            if event.key == pygame.K_ESCAPE:
                running_test = False
                return running_test
        