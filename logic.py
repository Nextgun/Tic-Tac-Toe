from drawer import *

# board needs to create the board and draw the board
# board needs to handle the logic
board_data = [["X","O","X"], 
              ["X","X","O"], 
              ["X","X","X"]]
print (board_data)
x = 0
y = 0
#print(board_data[x][y])
for y in range(0,3):
    for x in range(0,3):
        #print(x)
        #print(y)
        print(board_data[x][y])

# creates a list with all 9 rectangles 
# use to check collision in player input

width=1920
height=1080

#sets w to equal width of tile (scalable)
w = width/3
#sets h to equal height of tile (scalable)
h = height/3

Rect_list = []
for y in range(0,3):
    for x in range(0,3):
        Rect_list.append((x * w, y * h, w, h))
print (Rect_list)