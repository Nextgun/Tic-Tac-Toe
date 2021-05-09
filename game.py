import pygame, sys
from player import Player
from board import Game_Board 
from board import Tile

pygame.init()

# object creation
p1 = Player("X")
p2 = Player("O")

Tic_Tac_Toe = Game_Board()
Tic_Tac_Toe.draw_grid_lines()

Tic_Tac_Toe.get_position()

running = True # variable to keep the main loop running


# Main Loop
while running: 
    # look at every event in the queue
    for event in pygame.event.get():
        # did the user click the window close button? if so, stop the loop
        if event.type == pygame.QUIT:
            running = False
        # did the user hit a key?
        elif event.type == pygame.KEYDOWN:
            # was it the Escape Key? if so, stop the loop
            if event.key == K_ESCAPE:
                running == False

    
    #write code here that looks for player 1 input
    #write code here that looks for player 2 input
    # everythine will be drawn on the Tic_Tac_Toe.screen




    pygame.display.flip()
pygame.quit()



# j for y
for j in range(10):
    # i for x
    for i in range(10):
        pass

def looploop():
    for i in range(10,0,-2):
        print(i)

looploop()

print(1,2,3)
print(4,5,6)
print(7,8,9)