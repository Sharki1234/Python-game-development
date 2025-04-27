import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen : pgzero.screen.Screen
import random

WIDTH = 1000
HEIGHT = 1000

score = 0
add = 1
extras = ["flower","jerry","coin"]
actors = []
value = [1,20,100]
cheese = Actor("cheeze")
gap = WIDTH/len(extras)
def make_boosts():
    for num in extras:
        actors.append(Actor(num))
    
    for i in range(len(actors)):
        actors[i].y = gap*(i+1)
        actors[i].x = 800

def draw():
    screen.clear()
    screen.fill(color = (255,128,0))
    cheese.draw()
    screen.draw.text(score,center = (20,20),fontsize = 20)

def on_mouse_down(pos):
    global score
    if cheese.collidepoint(pos):
        score += add


pgzrun.go()