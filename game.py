import pygame, sys
#from player import *

from logic import *
from Draw import myDraw
import player as pl
#-------------------------------------------------------------------------

pygame.init()

# object creation
draw = myDraw()
p1 = pl.HumanPlayer("X")
p2 = pl.HumanPlayer("O")

current_player = p1

print("i am game module before the loop and I work")

screen = "game"
running = True # variable to keep the main loop running
# Main Loop
while running: 
    if screen == "title":
        # write title screen code here
        pass
    if screen == "game":
        # look at every event in the queue
        for event in pygame.event.get():
            # did the user click the window close button? if so, stop the loop
            if event.type == pygame.QUIT:
                running = False
            # did the user hit a key?
            if event.type == pygame.KEYDOWN:
                # was it the Escape Key? if so, stop the loop
                if event.key == pygame.K_ESCAPE:
                    running == False

            # draw board
            draw.Board()

            # get player input
            current_player.get_input(event)

            pygame.display.flip()
    if screen == "gameover":
        # write game over screen code here
        pass
pygame.quit()



    #write code here that looks for player 1 input
    #write code here that looks for player 2 input
    # everythine will be drawn on the Tic_Tac_Toe.screen
