import pygame
import logic


# draw will recieve input and proccessing all the drawing
# make functions for now. 
# later I will convert into a class

class myDraw():
    def __init__(self, width=1920, height=1080):
        self.board_size = 3
        self.width = width
        self.height = height
        self.w = self.width / self.board_size
        self.h = self.height / self.board_size
        
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill([255,255,255])

        self.grid_size = self.height / 3


   
    def Board(self):
        self.tile_shade()
        # draw the grid lines
        self.grid_lines()

        # draw board screen
            # write code to draw board screen here
            # draw the rect to check collisions
            # Board needs to iterate through the board data list 
            # and draw each players move accourding to position
        

    def tile_shade(self):
        # draws the white rectangles
        for i in range(0,9,2):
            pygame.draw.rect(self.screen, [255,255,255], logic.Rect_list[i], 0)
        # draws the gray rectangles
        for i in range(1,9,2):
            pygame.draw.rect(self.screen, [197,197,197], logic.Rect_list[i], 0)

    def grid_lines(self):
        # not the prettiest
        # draws grid lines, is scalable to screen size
        gridlines = [ [self.width * 1/3, 0, 2, self.height],
                    [self.width * 2/3, 0, 2, self.height],
                    [0, self.height * 1/3, self.width, 0], 
                    [0, self.height * 2/3, self.width, 0] ]
        for line in gridlines:
            pygame.draw.rect(self.screen, [0,0,0], line, 0)

    def Move(self):
        w = self.width / 3
        h = self.height / 3

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
        for row in range(self.board_size):
            for column in range(self.board_size):
                print("the row is ", row+1)
                print("the column is ", column+1)
                pos = self.board_data[row][column]
                print("position on board is ", pos)
                
  
    
    def draw(self):
        self.screen.draw.rect
                

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