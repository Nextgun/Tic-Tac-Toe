import pygame
import game_logic as gl
import player as pl
#-------------------------------------------------------------------------

pygame.init()

# object creation
TicTacToe = gl.TTT_Game()
p1 = pl.HumanPlayer("X")
p2 = pl.HumanPlayer("O")

# create variables
current_player = p1

print("i am game module before the loop and I work")

# Utility function 
# that I see myself using a lot
# Function that checks if the game is running
# if not running close game/app.
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
        


screen = "game" # Default screen that is drawn when the game starts
running = True # variable to keep the main loop running
# Main Loop
while running: 

    while screen == "title_screen":
        # wait for an event (left mouse click) to happen
        event = pygame.event.wait()
        # always check if running
        # if true continue
        # if false, close game
        running = check_if_running(event, running)
        if running == False:
            break
        # write title screen code here
        pygame.display.flip()
        
    while screen == "game":
        # wait for an event (left mouse click) to happen
        event = pygame.event.wait()
        # always check if running
        # if true continue
        # if false, close game
        running = check_if_running(event, running)
        if running == False:
            break
        
        TicTacToe.game_loop(event, current_player)
    
    while screen == "end_screen":
        # wait for an event (left mouse click) to happen
        event = pygame.event.wait()
        # always check if running
        # if true continue
        # if false, close game
        running = check_if_running(event, running)
        if running == False:
            break
        # write end screen code here
        pygame.display.flip()
        
pygame.quit()


