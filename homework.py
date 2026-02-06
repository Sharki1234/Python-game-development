import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 500
TITLE = "INFINITY GAUNTLET HOMEWORK"

infinity_gauntlet = Actor("infinity_gauntlet")
infinity_gauntlet.pos=(randint(0,500),250)

def draw():
    screen.clear()
    infinity_gauntlet.draw()

def update():
    if keyboard.left:
        infinity_gauntlet.x=infinity_gauntlet.x-10
        if infinity_gauntlet.x<=0:
            infinity_gauntlet.x=0
    if keyboard.right:
        infinity_gauntlet.x=infinity_gauntlet.x+10 
        if infinity_gauntlet.x>=500:
            infinity_gauntlet.x=500    
    if keyboard.up:
        infinity_gauntlet.y=infinity_gauntlet.y-10 
        if infinity_gauntlet.y>=500:
            infinity_gauntlet.y=500 
    if keyboard.down:
        infinity_gauntlet.y=infinity_gauntlet.y+10 
        if infinity_gauntlet.y>=500:
            infinity_gauntlet.y=500              















pgzrun.go()            