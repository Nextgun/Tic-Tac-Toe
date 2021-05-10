import pygame
from logic import *
# player needs to create the player and handle input
class Player():
    def __init__(self, icon):
        self.icon = icon

    def get_input(self, event):
        # checks if mouse button is clicked down
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: # left mouse button

                # loop through each tile available
                for rect in Rect_list: 
                    # check if the rect collides with the mouse pos
                    self.check_button_collision

def check_button_collision(self):
    if rect.collidepoint(pygame.mouse.get_pos()):
                            # if there is a collision
                            # get tile postion data
                            # update the board data with the new move
                            # draw the new board
                            pass
            
    
class AI():
    def __init__(self):
        pass
