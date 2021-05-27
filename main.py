import pygame # imports pygame
import Draw as D
import game_logic as gl # imports my game_logic module for tictactoe

#-------------------------------------------------------------------------

pygame.init() # initialize pygame

# object creation
TicTacToe = gl.TTT_Game() # creates a game of TicTacToe

# create variables
#current_player = p1
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
        



class Scenes():
    # creates variable to be used later
    current_player = None

    def __init__(self):
        self.event = None
        self.scene = "title_scene"

    def title_scene(self, event):
        # draw white screen
        D.create_white_Screen()

        # draw [Tic-Tac-Toe Background]


        # draw a play game button
        if D.play_button(event):
            # sets event to none so that nothing immediatly happens when you change scenes
            self.event = None

            self.scene = "game_scene" # changes the current scene

        # write title screen code here
        print("i am in", self.scene)
    
    def game_scene(self, event):
        
        game_state = "playing"
        info = TicTacToe.play_game(event)
        print("i am info list", info)
        if info == None:
            pass
        else:
            game_state, current_player = info

        if game_state == "over":
            self.scene = "end_scene"
        elif game_state == "draw":
            self.scene = "stalemate_scene"
            

    def end_scene(self, event):
        # draw [player [current player] won!]
        D.win_text()


        print("right before play again button in end scene ")
        if D.play_again_button(event): # draws a play again button
            print("insie play again button before setting scene to game")
            self.scene = "game_scene"
            print("insie play again button after setting scene to game")

        print("right before main menu button in end scene ")
        if D.main_menu_button(event): # draws a main menu button
            print("insie main menu button before setting scene to game")
            self.scene = "title_scene"
            print("insie main menu button after setting scene to game")
    
    def stalemate_scene(self, event):
        # draw [ its a draw! ] 
        D.draw_text()

        if D.play_again_button(event): # draw a play again button
            self.scene = "game_scene"
        
        if D.main_menu_button(event): # draw a main menu button
            self.scene = "title_scene"

    def scene_manager(self, event):
        self.event = event

        if self.scene == "title_scene":
            self.title_scene(self.event)
            #---------------------------------------------------------------------
        elif self.scene == "game_scene":
            self.game_scene(self.event)
            #---------------------------------------------------------------------
        elif self.scene == "end_scene":
            self.end_scene(self.event)
            #---------------------------------------------------------------------
        elif self.scene == "stalemate_scene":
            self.stalemate_scene(self.event)
            #---------------------------------------------------------------------

# object creation
the_game = Scenes()

if __name__ == "__main__":
    # Main Loop
    while running: 
        # grab the event
        event = pygame.event.wait()
        # check if running 
        running = check_if_running(event, running)
        # checks what scene it is currently and draws it
        the_game.scene_manager(event)
        # update the display
        pygame.display.flip()
    pygame.quit()

