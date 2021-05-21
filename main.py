import pygame # imports pygame
import sys
import game_logic as gl # imports my game_logic module for tictactoe
import player as pl # imports my player module for tictactoe
#-------------------------------------------------------------------------

pygame.init() # initialize pygame

# object creation
TicTacToe = gl.TTT_Game() # creates a game of TicTacToe
p1 = pl.HumanPlayer("X") # creates player 1, a human
p2 = pl.HumanPlayer("O") # creates player 2, a human

# create variables
current_player = p1

# Function that checks if the game is running; if not running, close game/app.
def check_if_running(event):
        # did the user click the window close button? if so, stop the loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # was it the Escape Key? if so, stop the loop
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        


current_screen = "game" # Default screen that is drawn when the game starts
running = True # variable to keep the main loop running
# Main Loop
while running: 
    
    #---------------------------------------------------------------------
    
    while current_screen == "title_screen":
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        running = check_if_running(event, running)
        if running == False:
            break
        
        # write title screen code here
        pygame.display.flip()
    
    #---------------------------------------------------------------------
    
    while current_screen == "game":
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        check_if_running(event)
     #   if running == False:
     #       break
        print("before screen = ttt.playgame")
        current_screen = TicTacToe.play_game(event, current_player, current_screen)
        print("after screen = ttt.playgame")
    #---------------------------------------------------------------------

    while current_screen == "end_screen":
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        running = check_if_running(event, running)
        if running == False:
            break
        
        # write end screen code here
        print("i am in end screen, inside while loop in main.py", current_screen)


        pygame.display.flip()
        
pygame.quit()


