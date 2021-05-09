
class Game_Board():
    def __init__(self, width=640, height=360):
        self.board_size = 3
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill([255,255,255])

        self.grid_size = self.height / 3
        self.board_data =  [["X"," "," "], 
                            [" "," ","O"], 
                            [" "," "," "]]

    def draw_icon(self):
        w = self.width / 3
        h = self.height / 3

        if icon == "X":
            #write code to draw x in pygame
            pass
        if icon == "O":
            #wite code to draw o in pygame
            pass
        
class Tile():
    def __init__(self):
            [ "X" ]

        
        
    
    def draw_Screen(self):
        return self.screen

    def draw_grid_lines(self):
        gridlines = [ [self.width * 1/3, 0, 2, self.height],
                      [self.width * 2/3, 0, 2, self.height],
                      [0, self.height * 1/3, self.width, 0], 
                      [0, self.height * 2/3, self.width, 0] ]
        for line in gridlines:
            pygame.draw.rect(self.screen, [0,0,0], line, 0)

    def create_game(self):
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
                
