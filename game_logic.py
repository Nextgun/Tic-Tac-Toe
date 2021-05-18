import pygame
import Draw as D

class TTT_Game():
    def __init__(self):
        self.create_board_data()
        self.Move_xy_pos = None

    def create_board_data(self):
        self.board_data = [[" "," "," "], 
                           [" "," "," "], 
                           [" "," "," "]]

    def update_board_data(self, move_xy_pos, player):
     #   print("inside update_board_data funciton")
        if move_xy_pos == None:
            return
        else:
            # sets x and y to be the info passed from the move_xy_pos tuple
            x,y = move_xy_pos[0], move_xy_pos[1]

            # checks if the clicked on tile is empty
            if self.board_data[y][x] == " ":
                # if empty write in player move
                self.board_data[y][x] = player.icon  

            # checks if player has icon X
            if player.icon == "X":
                # if so, change icon to O
                player.icon = "O"
                
            # checks if player has icon O
            elif player.icon == "O":
                # if so, change icon to X
                player.icon = "X"

    def check_win_condition(self, player_icon):
        # i want to loop through the tiles in board data
        # check if 3 Y's or 3 X's and the same icon
        #   if so, current player wins

        size_of_array = len(self.board_data) #length of board_data list
        # loop through using the size_of_array as the upperbounds of the loop
        for i in range(size_of_array):
            # logical test to see if game won or stalemate
            pass

        # iterates through the y axis
        for Y_axis in self.board_data:
            print("i am y axis in checkwinconddition:",Y_axis)
            #if self.board_data[0]

            for x_axis in Y_axis:
                print("i am x axis in checkwincondition", x_axis)
                if x_axis == player_icon:
                    # write code that checks if all the x values are the same icon
                    # if so, then you win
                    print("i am inside if x axis == player_icon")
                    pass
        # in order to iterate properly, i need to use board size as uppperbound
        # for i in range(0, boardsize):
        # inside i check if all are the same
        # if so , then win
        # else, i need to increment to check the second and third rows.
        # remember that I am trying to make my code scalable 
        # so the increment need to be math formulas, not hard code


        

            
    def game_loop(self, event_type, current_player):
        # draw board
        D.game_Board(self.board_data) 

        # get player input
        self.Move_xy_pos = current_player.get_input(event_type)
        #   print("in between self.move and self.update", self.Move_xy_pos)
        self.update_board_data(self.Move_xy_pos, current_player)
        self.check_win_condition(current_player.icon)

        pygame.display.flip()

thegametest = TTT_Game()
print (thegametest.board_data)

print ("i am logic module and I work")
print(" i am move pos: ",thegametest.Move_xy_pos)
thegametest.check_win_condition("X")