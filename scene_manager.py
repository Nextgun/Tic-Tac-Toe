import Draw as D
import game_logic as gl # imports my game_logic module for tictactoe
#-------------------------------------------------------------------------
# object creation
TicTacToe = gl.TTT_Game() # creates a game of TicTacToe

# Scenes class handles running the scenes 
class Scenes():
    def __init__(self):
        self.event = None
        self.scene = "title_scene" # starts the program at the title scene

        # creates variable to be used later
        self.current_player = None
            
        # creates a flag variable to draw the TTT backgound once
        self.is_background_drawn = False

    def title_scene(self, event):
        # draw [Tic-Tac-Toe Background] using a flag variable
        if self.is_background_drawn == False:
            D.draw_TTT_Background()
            self.is_background_drawn = True

        # checks if player pressed on the play game button
        if D.play_button(event):
            # sets event to none so that nothing immediatly happens when you change scenes
            self.event = None
            self.scene = "game_scene" # changes the current scene

        # write title screen code here
        print("i am in", self.scene)
    
    def game_scene(self, event):
        # sets game_state to playing to start the game
        game_state = "playing"

        # runs the game and return some info to use
        info = TicTacToe.play_game(event)

        # checks if the game has not ended
        if info == None:
            # if the game has not ended, do nothing
            pass
        else:
            # else, get info which is a list and split it into 2 variables
            game_state, self.current_player = info

        # checks if game ended by win
        if game_state == "over":
            self.scene = "end_scene" # changes the current scene
        # checks if game ended by draw
        elif game_state == "draw":
            self.scene = "stalemate_scene" # changes the current scene
            
    def end_scene(self, event):
        # draw [player [current player] won!]
        D.win_text()

        # checks if player pressed the play again button
        if D.play_again_button(event): # draws a play again button
            self.scene = "game_scene" # changes the current scene

        # checks if player pressed on the main menu button
        if D.main_menu_button(event): # draws a main menu button
            # resets variable to False so that the background gets redrawn
            self.is_background_drawn = False
            self.scene = "title_scene" # changes the current scene
    
    def stalemate_scene(self, event):
        # draw [ its a draw! ] 
        D.its_a_draw_text()

        # checks if player pressed the play again button
        if D.play_again_button(event): # draw a play again button
            self.scene = "game_scene" # changes the current scene
        
        # checks if player pressed on the main menu button
        if D.main_menu_button(event): # draw a main menu button
            # resets variable to False so that the background gets redrawn
            self.is_background_drawn = False
            self.scene = "title_scene" # changes the current scene

    def scene_manager(self, event):
        self.event = event

        # checks which scene the program is in and executes accordingly
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
