import pgzrun
import random
WIDTH = 800
HEIGHT = 500
ship = Actor("galaga")
ship.pos = (250,HEIGHT - 40)
bullets = []
bugs = []
gap = 60
over = False
direction = -1
def initiation():
    for i in range(4):
        row = []
        for j in range(7):
            bug = Actor("bug")
            bug.x = gap*(j+1)
            bug.y = i*40
            row.append(bug)
        bugs.append(row)
initiation()
def draw():
    screen.fill(color = "light blue")
    for row in bugs:
        for bug in row:
            bug.draw()
    ship.draw()
    for b in bullets:
        b.draw()
    if over:
        screen.fill(color = "black")
        screen.draw.text("GAMEOVER",(WIDTH/2-150,HEIGHT/2),fontsize = 70,color = "white")

def check(move_down):
    global over  
    if len(bugs) == 0:
        over = True 
    for row in bugs:
        if row == 0 :
            bugs.remove(row)  
    for row in bugs:
        for bug in row:
            bug.x+=direction*2
            if move_down:
                bug.y+=50
    
        for b in bullets[::]:
                b.y-=5
                if b.y<0:
                    bullets.remove(b)
                if b.colliderect(bug):
                    bullets.remove(b)

                    row.remove(bug) 
    
            

def update():
    global over,direction
    
    move_down = False
    if len(bugs) == 0:
        over = True   
    if len(bugs) != 0:
        if (bugs[0][-1].x>WIDTH or bugs[0][0].x<0):
            direction *= -1
            move_down = True 
    check(move_down )
   
    
            
            
            

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].pos = (ship.x,ship.y-20)
    if key == keys.LEFT:
        ship.x-=10
    if key == keys.RIGHT:
        ship.x+=7
    




pgzrun.go()