import pygame

# player needs to create the player and handle input
class HumanPlayer():
    def __init__(self, icon, player_num):
        self.player_num = player_num
        self.icon = icon

    def __str__(self):
        return f"I am player {self.player_num} and my icon is {self.icon}"

    def get_input(self, event):
    
        # checks if mouse button is clicked down
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: # left mouse button
                return self.check_button_collision()

                    

    def check_button_collision(self):
        # Imports the rectangles we drew; in Draw module to check for collision.
        from Draw import Rect_list
            
        # loop through each rect in grid
        for rect in Rect_list: 
            # check if the rect collides with the mouse pos
            
            # if there is a collision, checks each rectangle
            if rect.collidepoint(pygame.mouse.get_pos()):
             #   print(rect) # prints out rectangle info
                move_xy_pos = self.get_rect_xy(rect)
             #   print("i am testmovepos in the check collion",move_xy_pos)
                
                return move_xy_pos
      #      else:
      #          print("didnt find any collision")  

    
    def get_rect_xy(self, rect):
        # imports function ceil and variables tile_W, tile_H        
        from math import ceil
        from Draw import tile_W, tile_H

        # gets the rect x and converts into an int from 0-2
        tile_x_pos = ceil(rect[0]/tile_W) 

        # gets the rect y and converts into an int from 0-2
        tile_y_pos = ceil(rect[1]/tile_H) 

        return (tile_x_pos, tile_y_pos)
    

    # creates a list with all 9 rectangles 
    # rectangles needed to check collision 



            
            
    
class AI():
    def __init__(self):
        pass
