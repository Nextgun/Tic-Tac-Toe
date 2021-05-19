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
        score = 0
        Win = False
        size_of_array = len(self.board_data) #length of board_data list

        # i want to loop through the tiles in board data
        # check if 3 Y's or 3 X's and the same icon
        #   if so, current player wins


        #---------------------------------------------------------------------------

        # seperate into function. call it horizontal_check
        # win condition for  * * *    horizontal
        for y in range(size_of_array):
            for x in y:
                if self.board_data[y][x] == player_icon:
                    score += 1
                    if score == 3:
                        Win = True
            if score != 3:
                # reset score to 0 after every check
                score = 0

        #---------------------------------------------------------------------------

        # seperate into function. call it vertical_check
        #                      * 
        # win condition for    *      vertical
        #                      * 
        for x in range(size_of_array):
            for y in x:
                if self.board_data[y][x] == player_icon:
                    score += 1
                    if score == 3:
                        Win = True
            if score != 3:
                # reset score to 0 after every check
                score = 0

        #---------------------------------------------------------------------------

        # seperate into function. call it left_to_right_diagnal_check
        #                    *
        # win condition for    *      diagnal left to right
        #                        *
        for i in range(size_of_array):
            if self.board_data[i][i] == player_icon:
                score += 1
                if score == 3:
                    Win = True
        if score != 3:
            # reset score to 0 after every check
            score = 0

        #---------------------------------------------------------------------------

        # Need to redo this section of the logical test because it will not work,
        # also need to seperate all logical tests into seperate functions,
        # then need to test all the logical tests using those functions.

        # seperate into function. call it right_to_left_diagnal_check
        #                        *
        # win condition for    *      diagnal right to left
        #                    *  
        a = [ ]
        for A in range(size_of_array):
            a.append(A)
        for y in range(size_of_array):  # this section is not going to work because it is still in a nested loop. so it will iterate through entire grid
            for x in a:
                if self.board_data[y][x] == player_icon:
                    score += 1
                    if score == 3:
                        win = True
                    elif score != 3:
                        # reset score to 0 after every check
                        score = 0
        
        #---------------------------------------------------------------------------


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