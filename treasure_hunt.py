import random
#create board - 2d list
board = []
def board_creation():
    for i in range(3):
        row = []
        for i in range(3):
            row .append("x ")
        print(''.join(row))

#randomise coordinates where treasure is - part of list

def game():
    flag = False
    tries = 3
    y = random.randint(1,3)
    x = random.randint(1,3)
    while not flag:
        board_creation()
        user_row = int(input("What row?"))
        user_column = int(input("What column?"))
        if user_row == x and user_column == y:
            print("CORRECT")
            flag == True
        if user_column > y:
            print("Hint:go left")
            tries -= 1
        if user_column < y:
            print("Hint:go right")
            tries -=1
        if user_row > x:
            print("Hint:go up")
            tries -=1
        if user_row < x:
            print("Hint:go down")
            tries -=1


        # tries
        #hints up or down or left
game()