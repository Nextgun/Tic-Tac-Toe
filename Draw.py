import pygame



# draw will recieve input and proccessing all the drawing
# make functions for now. 
# later I will convert into a class

class myDraw():
    width = 640
    height = 360
    #def __init__(, width=640, height=360):
    board_size = 3
    #width = width
    #height = height
    w = width / board_size
    h = height / board_size
    
    screen = pygame.display.set_mode([width, height])
    screen.fill([255,255,255])

    grid_size = height / 3

    @classmethod
    def change_res(cls, w, h):
        witdh = w
        height = h

    # this code should create the screen and return it, currently not working, not implemented
    def Screen(width=640, height=360):
        screen = pygame.display.set_mode([width, height])
        screen.fill([255,255,255])
        #return screen

    def Board(self):
        #.Screen()
        
        # draws the shaded tiles
        self.tile_shade()
        # draw the grid lines
        self.grid_lines()

        # draw board screen
            # write code to draw board screen here
            # draw the rect to check collisions
            # Board needs to iterate through the board data list 
            # and draw each players move accourding to position
        
    def tile_shade(self):
        import logic as l
        # draws the white rectangles
        for i in range(0,9,2):
            pygame.draw.rect(myDraw.screen, [255,255,255], l.Rect_list[i], 0)
        # draws the gray rectangles
        for i in range(1,9,2):
            pygame.draw.rect(myDraw.screen, [197,197,197], l.Rect_list[i], 0)

    def grid_lines(self):
        # not the prettiest
        # draws grid lines, is scalable to screen size
        gridlines = [ [myDraw.width * 1/3, 0, 2, myDraw.height],
                      [myDraw.width * 2/3, 0, 2, myDraw.height],
                      [0, myDraw.height * 1/3, myDraw.width, 0], 
                      [0, myDraw.height * 2/3, myDraw.width, 0] ]
        for line in gridlines:
            pygame.draw.rect(myDraw.screen, [0,0,0], line, 0)

    def Move(self):
        w = width / 3
        h = height / 3

        if icon == "X":
            #write code to draw x in pygame
            pass
        if icon == "O":
            #wite code to draw o in pygame
            pass
        
    def Win_Screen(self):
        pass
    def Stalemate_Screen(self):
        pass



    def get_position(self):
        for row in range(board_size):
            for column in range(board_size):
                print("the row is ", row+1)
                print("the column is ", column+1)
                pos = board_data[row][column]
                print("position on board is ", pos)
                
  
    
    def fuckdraw(self):
        screen.draw.rect
                

        # j for y
        for j in range(10):
            # i for x
            for i in range(10):
                pass

        def looploop():
            for i in range(10,0,-2):
                print(i)

        #looploop()

        print(1,2,3)
        print(4,5,6)
        print(7,8,9)

print ("i am Draw module and I work")