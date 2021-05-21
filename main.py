import pygame # imports pygame
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
running = True # variable to keep the main loop running

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
        
        else:
            running_test = True
            return running_test
        



class GameScene():
    def __init__(self):
        self.scene = "title_scene"
    
    def title_scene(self):
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        running = check_if_running(event, running)
     #   if running == False:
     #       break
        
        # write title screen code here
        pygame.display.flip()
    
    def game_scene(self):
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        
        print("after running check: ", running)

     #   if running == False:
     #       break
        print("before screen = ttt.playgame")
        TicTacToe.play_game(event, current_player, current_screen)
        print("after screen = ttt.playgame")

    def end(self):
        # wait for event (left mouse click), assign it to a variable
        event = pygame.event.wait()
        
        # always check if running: if true continue; if false, close game
        running = check_if_running(event, running)
     #   if running == False:
     #       break
        
        # write end screen code here
        print("i am in end screen, inside while loop in main.py", current_screen)




game_scene = GameScene()








# Main Loop
while running: 
    event = pygame.event.wait()
    running = check_if_running(event, running)
    #---------------------------------------------------------------------
  #  game_scene.title_scene()
    #---------------------------------------------------------------------
    game_scene.game_scene()
    #---------------------------------------------------------------------
 #  game_scene.end()
    #---------------------------------------------------------------------
    print("right before pygame display flip")
    pygame.display.flip()
    print("outside while  current screen loop but inside running while")
pygame.quit()


