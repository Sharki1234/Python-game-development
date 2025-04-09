import pgzrun
import random
from pgzero.builtins import *
import pgzero.screen
screen:pgzero.screen.Screen
WIDTH = 500
HEIGHT = 500
score = 0
message = ""
mouse = Actor('jerry')
cheese = Actor('cheeze')
cheese.x = 250
cheese.y = 250
def draw():
    screen.blit("clouds acc",(0,0))
    mouse.draw()
    cheese.draw()
    message = (f"your score is: {score}")
    screen.draw.text(message,center = (50,20),fontsize = 20)

def update():
    global score,message
    if keyboard.left:
        mouse.x -=10
    elif keyboard.right:
        mouse.x +=10
    elif keyboard.up:
        mouse.y -=10
    elif keyboard.down:
        mouse.y +=10
    
    if mouse.colliderect(cheese):
        score+=1
        cheese.x = random.randint(0,500)
        cheese.y = random.randint(0,500)


pgzrun.go()