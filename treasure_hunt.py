import random
#create board - 2d list
board = []
def board_creation():
    for i in range(3):
        row = []
        for i in range(3):
            row .append("x ")
        board.append(row)
        print(''.join(row))

#randomise coordinates where treasure is - part of list
def coordinates():
    board_creation()
    y = random.randint(0,2)
    x = random.randint(0,2)
    return x,y
#check if right
def check():
    x,y = coordinates()
    user_row = int(input("What row?"))
    user_column = int(input("What column?"))
    
# tries
#hints up or down or left

