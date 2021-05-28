import pygame
import Draw as D
import player as pl # imports my player module for tictactoe
import time

max_amounts_of_moves = D.BOARD_SIZE * D.BOARD_SIZE

p1 = pl.HumanPlayer("X", 1) # creates player 1, a human
p2 = pl.HumanPlayer("O", 2) # creates player 2, a human

print(p1)
print(p2)



class TTT_Game():
    def __init__(self):
        self.create_board_data()
        self.Move_xy_pos = None
        self.current_player = p1
        self.move_count = 0

    # a scalable function to create our board data
    def create_board_data(self):
        self.board_data = []
        xboardData = []
        for y in range(D.BOARD_SIZE):
            xboardData = []
            self.board_data.append(xboardData)
            for x in range(D.BOARD_SIZE):
                xboardData.append(" ")

    # updates board data after a player makes a move
    def update_board_data(self, move_xy_pos, player_icon):
     #   print("inside update_board_data funciton")
        if move_xy_pos == None:
            return
        else:
            # sets x and y to be the info passed from the move_xy_pos tuple
            x,y = move_xy_pos[0], move_xy_pos[1]

            # checks if the clicked on tile is empty
            if self.board_data[y][x] == " ":
                # if empty write in player move
                self.board_data[y][x] = player_icon  

            # checks if tile is filled, if so skip it
            else:
                # I skip the tile by 
                D.invalid_move_text()

                self.move_count -= 1 # decrement the move counter by 1
                time.sleep(0.8) # small delay for player to read image

                # Swaps here to opposite player to get 
                # reswapped back to current player later in the code.
                self.swap_current_player(move_xy_pos)

    # checks horizontal win
    def horizontal_check(self, player_icon, size_of_array, score, Win):
        # win condition for  * * *    horizontal

        # loops through each horizontal plane to check win
        for y in range(size_of_array):
            for x in range(size_of_array):
                if self.board_data[y][x] == player_icon:
                    # if icon in grid pos = player icon; increment score
                    score += 1
                    # when score is enough points, you win
                    if score == size_of_array:
                        Win = True
                        break

            # checks if you DID NOT acheive enough points to win
            if score != size_of_array:
                # reset score to 0 after every check
                score = 0

        return Win

    # checks vertical win
    def vertical_check(self, player_icon, size_of_array, score, Win):

        #                      * 
        # win condition for    *      vertical
        #                      * 

        # loops through each vertical plane to check win
        for x in range(size_of_array):
            for y in range(size_of_array):
                if self.board_data[y][x] == player_icon:
                    # if icon in grid pos = player icon; increment score
                    score += 1
                    # when score is enough points, you win
                    if score == size_of_array:
                        Win = True
                        break

            # checks if you DID NOT acheive enough points to win
            if score != size_of_array:
                # reset score to 0 after every check
                score = 0

        return Win
    # checks left to right diagnal win
    def left_to_right_diagnal_check(self, player_icon, size_of_array, score, Win):
        #                    *
        # win condition for    *      diagnal left to right
        #                        *

        # loops through the diagnal to check icons on grid
        for i in range(size_of_array):
            if self.board_data[i][i] == player_icon:
                # if icon in grid pos = player icon; increment score
                score += 1
                # when score is enough points, you win
                if score == size_of_array:
                    Win = True
                    break

        # checks if you DID NOT acheive enough points to win
        if score != size_of_array:
            # reset score to 0 after every check
            score = 0

        return Win

    # checks right to left diagnal win
    def right_to_left_diagnal_check(self, player_icon, size_of_array, score, Win):
        #                        *
        # win condition for    *      diagnal right to left
        #                    *  

        # create T, subtract 1 to account that indexes start at 0 not 1 
        T = size_of_array -1

        # loops through the diagnal to check icons on grid
        for y in range(size_of_array):  
            if self.board_data[y][T] == player_icon:
                # if icon in grid pos = player icon; increment score
                score += 1
                # when score is enough points, you win
                if score == size_of_array:
                    Win = True
                    break
                # each iteration subtract 1 from T until a reaches zero
                T -= 1
              
        # checks if you DID NOT acheive enough points to win
        if score != size_of_array:
            # reset score to 0 after every check
            score = 0
            
        return Win

    # function with all win conditions functions together
    def win_conditions_grouped_together(self, current_player_icon, size_of_array, score, Win):
        #---------------------------------------------------------
        Win = self.vertical_check(current_player_icon, size_of_array, score, Win)  
        if Win == True:
            return Win                  
        #---------------------------------------------------------
        Win = self.left_to_right_diagnal_check(current_player_icon, size_of_array, score, Win)
        if Win == True:
            return Win       
        #---------------------------------------------------------
        Win = self.right_to_left_diagnal_check(current_player_icon, size_of_array, score, Win)
        if Win == True:
            return Win       
        #---------------------------------------------------------
        Win = self.horizontal_check(current_player_icon, size_of_array, score, Win)
        if Win == True:
            return Win       
        #---------------------------------------------------------

    def swap_current_player(self, move_xy_pos):
        # if there was no player move, do nothing
        if move_xy_pos == None:
            pass
        # if there was a player move, run code
        else:
            # checks if it is player 1
            if self.current_player == p1:
                # if so, change to player 2 
                self.current_player = p2
                
            # checks if it is player 2
            elif self.current_player == p2:
                # if so, change to player 1
                self.current_player = p1

    def reset_game_board(self):
        for y in range(D.BOARD_SIZE):
            for x in range(D.BOARD_SIZE):
                if self.board_data[y][x] != " ":
                    # if empty write in player move
                    self.board_data[y][x] = " "

    def check_win_condition(self, move_xy_pos, current_player):
        # if there was no player move, do nothing
        if move_xy_pos == None:
            return
        # if there was a player move, run code
        else:
            # creates variables to be used to check win conditions
            score = 0
            Win = False
            size_of_array = len(self.board_data) #length of board_data list

            # when Win is False, run all checks
            if Win == False:
                # runs the win condition functions to check if someone won
                Win = self.win_conditions_grouped_together(current_player.icon, size_of_array, score, Win)

            # if Win returns True, execute win function and win screen
            if Win == True:
                # resets the game board data to be at starting position
                self.reset_game_board()
                # resets the draw counter to be at starting postion
                self.move_count = 0
                return "over"

    # counts how many moves have been made to check for a draw
    def count_moves(self, move_xy_pos):
        if move_xy_pos == None:
            pass
        else:
            # increment the move counter for every move taken
            self.move_count += 1
            # checks if the max amount of moves have been played
            if self.move_count == max_amounts_of_moves:
                # if the game draws reset move count to starting postion
                self.move_count = 0
                # reset game board data to starting position
                self.reset_game_board()
                return "draw"

    def play_game(self, event_type):

        
        # get player input
        self.Move_xy_pos = self.current_player.get_input(event_type)

        # updates board data with player move and player icon
        self.update_board_data(self.Move_xy_pos, self.current_player.icon)

        # draw board / game screen
        D.game_screen(self.board_data) 

        # checks if the current player has won
        game_state_check = self.check_win_condition(self.Move_xy_pos, self.current_player)
        if game_state_check == "over":
            info = ["over", self.current_player]
            return info

        # checks if moves equals maximum amount, if so, stalemate
        game_state_check = self.count_moves(self.Move_xy_pos)
        if game_state_check == "draw":
            info = ["draw", self.current_player]
            return info
            
        # if the player did not win, swap the current player
        self.swap_current_player(self.Move_xy_pos)
    
        # updates screen to reflect new changes; (updates next frame)
        pygame.display.flip()
