import pgzrun
TITLE = "GAME"
HEIGHT = 500
WIDTH = 500
def draw():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(X)
        matrix.append(row)
        screen.draw.circle((200,100),30,color = "red")






pgzrun.go()