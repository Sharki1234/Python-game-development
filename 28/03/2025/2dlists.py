
def print_board():
    for i in range(3):
        print(" | ".join(board[i]))
        print("-"*10)

board = []

def initialising():
    for i in range(3):
        rows = []
        for j in range(3):
            rows.append(" ")
        board.append(rows)

def game():
    initialising()
    player = "X"
    game_over = False
    print_board()

    while not game_over:
        ask = int(input("what row?"))
        ask_column = int(input("what column?"))
        if ask>2 or ask_column>2  or board[ask][ask_column] != " ":
            print("pls chose the columns available")
            continue
        board[ask][ask_column] = player
        print_board()

        if check():
            print(f"{player}has won")
            game_over = True
        else:
            if check_tie():
                game_over = True
                print("it's a tie")
            
        player = "O" if player == "X" else "X"


def check():
     
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
        
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            
            return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        
        return True
    if board[0][0] == board[1][1] == board[2][2] != " " :
       
        return True
    return False

def check_tie():
    for i in range(3):
        for w in range(3):
            if board[i][w] == " ":
                return False
    return True
game()