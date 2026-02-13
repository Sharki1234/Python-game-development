import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 500
TITLE = "RAINDROP ANIMATIONAL SCENE(RAS)"

bg=Actor("bg")
bg.pos=(250,250)
#create a list by using a for loop
raindrops = []
for i in range(10):
    raindrop=Actor("raindrop")
    raindrop.x=randint(0,500)
    raindrop.y=randint(0,500)
    raindrops.append(raindrop)

def draw():
    bg.draw()
    for raindrop in raindrops:
        raindrop.draw()

def update():
    screen.clear()
    for raindrop in raindrops:
        raindrop.y+=7
        if raindrop.y>500:
            raindrop.y=65
            raindrop.x=randint(0,500)

pgzrun.go()