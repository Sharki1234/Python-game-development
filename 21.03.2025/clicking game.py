import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen : pgzero.screen.Screen

add = 1
WIDTH = 500
HEIGHT = 500

score = 0
extras = ["jerry","flower","alien"]
actors = []
value = [1,20,100]
cheese = Actor("cheeze")
gap = WIDTH/(len(extras)+1)
message = ""
def make_boosts():
    for num in extras:
        actors.append(Actor(num))
    
    for i in range(len(actors)):
        actors[i].y = gap*(i+1)
        actors[i].x = (HEIGHT/10)*8

# def boosts():
#     if score >= 10:
#         return 1
#     if score >=100:
#         return 2
#     if score >= 1000:
#         return 3

make_boosts()
#boosts()

def draw():
    screen.clear()
    screen.fill(color = (205,108,0))
    cheese.x = WIDTH/2
    cheese.y = HEIGHT/2
    cheese.draw()
    message = (f"you're score is:{score}")
    screen.draw.text(message,center = (50,20),fontsize = 20)
    if score >= 10:
        actors[0].draw()
    if score >=100:
        actors[1].draw()
    if score >= 1000:
        actors[2].draw()

def on_mouse_down(pos):
    global score,add
    
    for i in range(len(actors)):
            if actors[0].collidepoint(pos):
                add = 10
            if actors[1].collidepoint(pos):
                add = 100
            if actors[2].collidepoint(pos):
                add = 1000
    
    if cheese.collidepoint(pos):
        score += add
    

        
        


pgzrun.go()