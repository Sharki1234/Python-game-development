import pgzrun
WIDTH = 500
HEIGHT = 410
board = []
x = WIDTH/3
y = HEIGHT/3
user = "X"
ouserposx = []
xuserposx = []
userposx = []
userposy = []
ouserposy = []
xuserposy = []
userdrawn = []

gameover = False
def initialising():
    for i in range(3):
        recs = []
        for j in range(3):
            rect2 = Rect((0,0),(x,y))
            rect2.center = (x/2+(x*i),y/2+(y*j))
            recs.append(rect2)
        board.append(recs)
initialising()
def draw():
    for rec in board:
        for r in rec:
            screen.draw.filled_rect(r,(161,249,148))
    for i in range (len(userdrawn)):
        screen.draw.text(userdrawn[i],(userposx[i],userposy[i]),fontsize=30,color = "black")
    if gameover == True:
        screen.fill(color = "black")

def on_mouse_down(pos):
    global user,gameover
    for recs  in board:
        for r in recs:
            if r.collidepoint(pos):
                userposx.append(r.x)
                userposy.append(r.y)
                
                userdrawn.append(user)
                print(userdrawn)
                print(userposx)
                print(userposy)
                user = "O" if user == "X" else "X"
                if user == "O":
                    ouserposy.append(r.y)
                    ouserposx.append(r.x)
    for i in ouserposx:
        c = ouserposx.count(i)
        if c == 3:
            gameover = True
    print(c)





pgzrun.go()