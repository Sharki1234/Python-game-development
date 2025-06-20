import pgzrun
import random
WIDTH = 500
HEIGHT = 500
ship = Actor("galaga")
ship.pos = (250,HEIGHT - 40)
bullets = []
bugs = []
gap = 60
over = False
def initiation():
    for i in range(7):
        bug = Actor("bug")
        bug.y = -10
        bug.x = gap*(i+1)
        bugs.append(bug)
initiation()
def draw():
    screen.fill(color = "light blue")
    for n in bugs:
        n.draw()
    ship.draw()
    for b in bullets:
        b.draw()
    if over:
        screen.fill(color = "black")
        screen.draw.text("GAMEOVER",(WIDTH/2-150,HEIGHT/2),fontsize = 70,color = "white")

def update():
    global over
    for bug in bugs:
        if bug.y != HEIGHT:
            bug.y += 1
        
            
        else:
           over = True 
    
        for b in bullets[::]:
            b.y-=5
            if b.y<0:
                bullets.remove(b)
            if b.colliderect(bug):
                bullets.remove(b)
                bugs.remove(bug)
            
            
            

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].pos = (ship.x,ship.y-20)
    if key == keys.LEFT:
        ship.x-=10
    if key == keys.RIGHT:
        ship.x+=7
    




pgzrun.go()