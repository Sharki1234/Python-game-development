board = []
for i in range(3):
    rows = []
    for j in range(3):
        rows.append(" ")
    board.append(rows)

def print_board():
    for i in range(3):
        print(" | ".join(board[i]))
        print("-"*10)

print_board()