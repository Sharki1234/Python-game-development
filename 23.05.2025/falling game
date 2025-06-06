import pgzrun
import random
from pgzero.builtins import *
import pgzero.screen
screen:pgzero.screen.Screen
WIDTH = 500
HEIGHT = 500
colours = [(83, 125, 93),(115, 148, 107),(158, 188, 138),(210, 208, 160),(0,0,0),(0,0,0)]
recs = []
score = 0
c = []
lives = 3
animation = []
gameover = False
user = Rect((0,0),(40,40))
user.center = (random.randint(20,WIDTH),HEIGHT-20)
def initiation():
    if not gameover:
        if recs[len(recs)-1].y>=HEIGHT/4:
            cc = random.choice(colours)
            c.append(cc)
            rect = Rect((0,0),(20,20))
            rect.center=(random.randint(10,WIDTH),10)
            recs.append(rect)
cc = random.choice(colours)
c.append(cc)
rect = Rect((0,0),(20,20))
rect.center=(random.randint(10,WIDTH),10)
recs.append(rect)   



def draw():
    screen.fill(color = (193, 225, 193))
    if lives>0:
        initiation()
        for i in range(len(recs)):
            screen.draw.filled_rect(recs[i],c[i])
        screen.draw.filled_rect(user,(0,0,0))
        screen.draw.text(str(score),center = (20,20),fontsize = 20)
   
for x in recs:
     ani = animate(x,duration = 10,y = HEIGHT)
     animation.append(ani)
    

def update():
    global lives,score
    if lives == 0:
        gameover = True
    else:
        if keyboard.left:
            user.x-=5
        if keyboard.right:
            user.x+=5
        for i in range(len(recs)):
            if user.colliderect(recs[i]):
                #animation.pop(i)
                if c[i]==(0,0,0):
                    lives-=3
                else:
                    score+=1
                    
        if lives == 0:
            gameover= True

pgzrun.go()