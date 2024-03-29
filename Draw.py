import pygame
from easygui import enterbox
# draw will recieve input and proccessing all the drawing
# make functions for now. 
# later I will convert into a class, maybe

WIDTH = 640 # Default width 
HEIGHT = 360 # Default height

Header = "Awesome Sauce Tic-Tac-Toe Game For Gamers"

BOARD_SIZE = enterbox("Type in a number for the size of the Tic-Tac-Toe board: ", Header)           
while True:
    if BOARD_SIZE.isnumeric():
        if int(BOARD_SIZE) < 21:
            break
        else:
            BOARD_SIZE = enterbox("uh oh, that number is too big, try a smaller one: ", Header)
    elif not BOARD_SIZE.isnumeric():
        BOARD_SIZE = enterbox("uh oh, thats not a number, try again: ", Header)
        
BOARD_SIZE = int(BOARD_SIZE) # Default board size

tile_W = WIDTH / BOARD_SIZE # creating relative width and height variables 
tile_H = HEIGHT / BOARD_SIZE # used to draw everything by scale rather then coordinates

# creates the screen to draw everything on
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
# creates a caption for the window
pygame.display.set_caption("Awesome Sauce Tic-Tac-Toe Game For Gamers")
# fills the screen with the color white
SCREEN.fill([255,255,255])

# creates the rectangles needed for logic and drawing and player
Rect_list = []
for y in range(BOARD_SIZE):
    for x in range(BOARD_SIZE):
        Rect_list.append(pygame.Rect(x * tile_W, y * tile_H, tile_W, tile_H))
print (Rect_list)


#_____________________________________________________________________________________
# this section of code handles the drawing for the game_scene

# creates white screen to then redraw on top
def create_white_Screen(WIDTH=640, HEIGHT=360):
    SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
    SCREEN.fill([255,255,255])
    #return SCREEN

# Draws the shading in the rectangles.
AMOUNT_OF_TILES = BOARD_SIZE * BOARD_SIZE
def tile_shade():
    # draws the white rectangles
    for rectangle in range(0,AMOUNT_OF_TILES,2):
        pygame.draw.rect(SCREEN, [255,255,255], Rect_list[rectangle], 0)

    # draws the gray rectangles
    for rectangle in range(1,AMOUNT_OF_TILES,2):
        pygame.draw.rect(SCREEN, [197,197,197], Rect_list[rectangle], 0)


ALL_LINES = []

def create_vertical_lines():
    counter = 1
    for num_Lines in range(BOARD_SIZE):
        line = (WIDTH * (counter/BOARD_SIZE), 0, 2, HEIGHT)
        ALL_LINES.append(line)
        counter += 1
# calls the function so that the lines are created an exist
create_vertical_lines()

def create_horizontal_lines():
    counter = 1
    for num_Lines in range(BOARD_SIZE):
        line = (0, HEIGHT * (counter/BOARD_SIZE), WIDTH, 0)
        ALL_LINES.append(line)
        counter += 1
# calls the function so that the lines are created an exist
create_horizontal_lines()

def grid_lines():
    for line in ALL_LINES:
        pygame.draw.rect(SCREEN, [0,0,0], line, 0)


# Iterates through board_data, and DRAWS player moves accordingly.
def player_moves_on_board(board_data):
    # nested loop to iterate through board_data info
    for y_row in range(BOARD_SIZE):
        for x_column_icon in range(BOARD_SIZE):

            # sets y to be an int to use in drawing function 
            y = y_row
            # sets x to be an int to use in drawing function
            x = x_column_icon 

            # sets current icon according to board position
            icon = board_data[y][x]
            
            # if icon in board_data is X, draws X
            if icon == "X":
               draw_X(x,y)
            
            # if icon in board_data is O, draws O
            if icon == "O":
                draw_O(x,y)
            else:
                pass

# Function that draws an X on the ttt board.
def draw_X(x,y):
    # calculates start and end position for first line
    start_pos =  ( ( (x * tile_W) + (tile_W * 0.25) ) , ( (y * tile_H) + (tile_H * 0.25 ) ) )
    end_pos =    ( ( (x * tile_W) + (tile_W * 0.75) ) , ( (y * tile_H) + (tile_H * 0.75 ) ) )
    
    # calculates start and end position for second line
    start_pos2 = ( ( (x * tile_W) + (tile_W * 0.75) ) , ( (y * tile_H) + (tile_H * 0.25 ) ) )
    end_pos2 =   ( ( (x * tile_W) + (tile_W * 0.25) ) , ( (y * tile_H) + (tile_H * 0.75 ) ) )

    # sets the constant for the width of all lines
    line_width = 7

    # draws both lines for the X icon
    pygame.draw.line(SCREEN, (0,0,0), start_pos, end_pos, line_width)
    pygame.draw.line(SCREEN, (0,0,0), start_pos2, end_pos2, line_width)
# Function that draws an O on the ttt board.
def draw_O(x,y):
    # calculates the center of the circle
    center = (int((x * tile_W) + (tile_W/2)), int((y * tile_H) + (tile_H/2)))
    
    # sets circle width
    circle_width = 7

    # Checks and chooses whether to make the circle 
    # using x or y information 
    # depending on screen size so that it scales properly.
    if tile_H > tile_W:
        circle_radius = int( (tile_W/2) - (0.1 * tile_W) )
    elif tile_H < tile_W:
        circle_radius = int( (tile_H/2) - (0.1 * tile_H) )
    
    # draws the circle for the O icon
    pygame.draw.circle(SCREEN, (0,0,0), center, circle_radius, circle_width)

def game_screen(board_data):
    # Resets screen to white before 
    # drawing anything else on top.
    create_white_Screen()
    
    # calls function to draws the shaded tiles
    tile_shade()

    # calls function to draw the grid lines
    grid_lines()

    # calls function that draws the players moves (X or O)
    player_moves_on_board(board_data)

#_____________________________________________________________________________________
# this section of code handles the drawing for the end and stalemate scenes

# play button
def play_button(event):
    # sets the x and y variables to draw everything in the same position
    x,y = WIDTH * 0.25, HEIGHT * 0.416 + HEIGHT * 0.0416

    # creates rectangle used for the collision
    Rect = pygame.Rect(x, y, WIDTH * 0.5, HEIGHT * 0.166)
    pygame.draw.rect(SCREEN, (255,255,255), Rect, 0) # draws the rectangle/button as white onto screen
    
    draw_image = pygame.image.load("image_ttt/play_game_small.png") # loads the image so pygame can draw it
    SCREEN.blit(draw_image, (x, y)) # draws the image onto the screen

    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws a black border around the button

    # checks if mouse button is clicked down
    if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: # left mouse button
            # if there is a collision between where the player clicked and the button
            if Rect.collidepoint(pygame.mouse.get_pos()):
                return True

# play again button
def play_again_button(event):
    # sets the x and y variables to draw everything in the same position
    x,y = WIDTH * 0.25, HEIGHT * 0.416 + HEIGHT * 0.0416

    # creates rectangle used for the collision
    Rect = pygame.Rect(x, y, WIDTH * 0.5, HEIGHT * 0.166)
    pygame.draw.rect(SCREEN, (255,255,255), Rect, 0) # draws the rectangle/button as white onto screen
   
    draw_image = pygame.image.load("image_ttt/play_again_small.png") # loads the image so pygame can draw it
    SCREEN.blit(draw_image, (x, y)) # draws the image onto the screen

    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws a black border around the rectangle

    # checks if mouse button is clicked down
    if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: # left mouse button
            # if there is a collision between where the player clicked and the button
            if Rect.collidepoint(pygame.mouse.get_pos()):
                return True

# main menu button 
def main_menu_button(event):
    # sets the x and y variables to draw everything in the same position
    x,y = WIDTH * 0.25, HEIGHT * 0.75 - HEIGHT * 0.0416

    # creates rectangle used for the collision
    Rect = pygame.Rect(x, y, WIDTH * 0.5, HEIGHT * 0.166)
    pygame.draw.rect(SCREEN, (255,255,255), Rect, 0) # draws the rectangle as white onto screen
    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws a black border around the rectangle

    draw_image = pygame.image.load("image_ttt/main_menu_small.png")# loads the image so pygame can draw it
    SCREEN.blit(draw_image, (x, y)) # draws the image onto the screen
  
    # checks if mouse button is clicked down
    if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.button == 1: # left mouse button
            # if there is a collision between where the player clicked and the button
            if Rect.collidepoint(pygame.mouse.get_pos()):
                return True

# draws Tic-Tac-Toe
def draw_TTT_Background():
    ttt_image = pygame.image.load("image_ttt/tictactoe_background.png") # loads the ttt background image
    SCREEN.blit(ttt_image, (0,0)) # draws the background

# draws the It's a Draw! text
def its_a_draw_text():
    x,y = WIDTH * 0.166, HEIGHT * 0.0416

    Rect = pygame.Rect(x, y, WIDTH * 0.666, HEIGHT * 0.333) # creates rectangle to draw border on

    draw_image = pygame.image.load("image_ttt/its_a_draw.png") # loads the its a draw text
    SCREEN.blit(draw_image, (x,y)) # draws the its a draw text

    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws black border 

# draws the Someone Won text
def win_text():
    x,y = WIDTH * 0.166, HEIGHT * 0.0416

    Rect = pygame.Rect(x, y, WIDTH * 0.666, HEIGHT * 0.333) # creates rectangle to draw border on

    win_image = pygame.image.load("image_ttt/someone_won.png") # loads the win text
    SCREEN.blit(win_image, (x,y)) # draws the win text

    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws black border 

# draws text on screen saying "the move you just tried to make is invalid try again"
def invalid_move_text():
    x,y = WIDTH * 0.166, HEIGHT * 0.0416

    Rect = pygame.Rect(x, y, WIDTH * 0.666, HEIGHT * 0.333) # creates rectangle to draw border on

    invalid_image = pygame.image.load("image_ttt/invalid_move.png") # loads the invalid move image
    SCREEN.blit(invalid_image, (x,y)) # draws invalid move image

    pygame.draw.rect(SCREEN, (0,0,0), Rect, 3) # draws black border 
    pygame.display.flip() # updates display


# unused code
def change_resolution(new_W, new_H):
    WIDTH = new_W
    HEIGHT = new_H

# Draws the lines that divide the grid>
def old_grid_lines():
    # draws grid lines, is scalable to SCREEN size
    # line info is actually a rectangle
    # order is:          x pos      , y pos       , width, height
    gridlines_rects = [ [WIDTH * 1/3, 0           , 2    , HEIGHT],
                        [WIDTH * 2/3, 0           , 2    , HEIGHT],
                        [0          , HEIGHT * 1/3, WIDTH, 0], 
                        [0          , HEIGHT * 2/3, WIDTH, 0]      ]

    # Iterates through the lines in gridlines list
    # and draws them.
    for line in gridlines_rects:
        pygame.draw.rect(SCREEN, [0,0,0], line, 0)