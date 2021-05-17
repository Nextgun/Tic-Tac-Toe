import pygame
# draw will recieve input and proccessing all the drawing
# make functions for now. 
# later I will convert into a class, maybe

WIDTH = 640 # Default width 
HEIGHT = 360 # Default height
BOARD_SIZE = 3 # Default board size

tile_W = WIDTH / BOARD_SIZE # creating relative width and height variables 
tile_H = HEIGHT / BOARD_SIZE # used to draw everything by scale rather then coordinates

# creates the screen to draw everything on
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
SCREEN.fill([255,255,255])

# creates the rectangles needed for logic and drawing and player
Rect_list = []
for y in range(0,3):
    for x in range(0,3):
        Rect_list.append(pygame.Rect(x * tile_W, y * tile_H, tile_W, tile_H))
print (Rect_list)


def game_Board(board_data):
    # Resets screen to white before 
    # drawing anything else on top.
    create_white_Screen()
    
    # calls function to draws the shaded tiles
    tile_shade()

    # calls function to draw the grid lines
    grid_lines()

    # calls function that draws the players moves (X or O)
    player_moves_on_board(board_data)

def change_resolution(new_W, new_H):
    WIDTH = new_W
    HEIGHT = new_H

# this code should create the SCREEN and return it, currently not working, not implemented
def create_white_Screen(WIDTH=640, HEIGHT=360):
    SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
    SCREEN.fill([255,255,255])
    #return SCREEN

# Draws the shading in the rectangles.
def tile_shade():
    # draws the white rectangles
    for i in range(0,9,2):
        pygame.draw.rect(SCREEN, [255,255,255], Rect_list[i], 0)
    # draws the gray rectangles
    for i in range(1,9,2):
        pygame.draw.rect(SCREEN, [197,197,197], Rect_list[i], 0)

# Draws the lines that divide the grid>
def grid_lines():
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

# Iterates through board_data, 
# and DRAWS player moves if available 
# for each position on board.
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

def Win_Screen(self):
    pass
def Stalemate_Screen(self):
    pass



def get_position(self):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            print("the row is ", row+1)
            print("the column is ", column+1)
            pos = board_data[row][column]
            print("position on board is ", pos)

print ("i am Draw module and I work")
