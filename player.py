import pygame
import logic as l

# player needs to create the player and handle input
class HumanPlayer():
    def __init__(self, icon):
        self.icon = icon

    def get_input(self, event):
        # checks if mouse button is clicked down
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: # left mouse button

                # loop through each tile available
                for rect in l.Rect_list: 
                    print("i am in the rectlist loop")
                    # check if the rect collides with the mouse pos
                    self.check_button_collision(rect)

    def check_button_collision(self,Rectangle):
        print ("i am in check button collision function")
        # if there is a collision, checks each rectangle
        if Rectangle.collidepoint(pygame.mouse.get_pos()):
            print(Rectangle.collidepoint) # prints out the collion info
            print(Rectangle) # prints out rectangle info
            # update board data here
            
            # use rectangle info to edit the logic rect_list and update to draw it
                                # get tile postion data
                                # update the board data with the new move
                                # draw the new board
        else:
            print("didnt find any collision")                       
                                
            
            
    
class AI():
    def __init__(self):
        pass
