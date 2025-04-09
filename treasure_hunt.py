import random
#create board - 2d list
board = []
def board_creation():
    for i in range(3):
      row = []
      for i in range(3):
        row .append("x ")
        board.append(row)
      print(''.join(board[i]))

#randomise coordinates where treasure is - part of list

def game():
    flag = False
    tries = 3
    board_creation()
    y = random.randint(0,2)
    x = random.randint(0,2)
    user_row = int(input("What row?"))
    user_column = int(input("What column?"))
    while not flag:
        board_creation()
        if user_row == x and user_column == y:
            print("CORRECT")
            flag == True
        if user_column > y:
            print("Hint:go up")
            tries -= 1
        if user_column < y:
            print("Hint:go down")
            tries -=1
        if user_row > x:
            print("Hint:go left")
            tries -=1
        if user_row < x:
            print("Hint:go right")
            tries -=1


        # tries
        #hints up or down or left
game()