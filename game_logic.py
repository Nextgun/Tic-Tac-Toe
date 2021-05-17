import pygame
import Draw as D

class TTT_Game():
    def __init__(self):
        self.create_board_data()
        self.Move_xy_pos = None

    def create_board_data(self):
        self.board_data = [["X","X","X"], 
                           ["O"," ","O"], 
                           ["X","O","X"]]

    def update_board_data(self, move_xy_pos):
     #   print("inside update_board_data funciton")
        if move_xy_pos == None:
            return
        else:
            print("after the return if statement")
            print(move_xy_pos)
            x = move_xy_pos[0]
            y = move_xy_pos[1]
            print(x)
            print(y)
            
        

    def check_win_condition(self, player_icon):
        # i want to loop through the tiles in board data
        # check if 3 Y's or 3 X's and the same icon
        #   if so, current player wins

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
            self.update_board_data(self.Move_xy_pos)

            pygame.display.flip()

thegametest = TTT_Game()
print (thegametest.board_data)

print ("i am logic module and I work")
print(" i am move pos: ",thegametest.Move_xy_pos)
thegametest.check_win_condition("X")