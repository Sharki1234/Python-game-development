import pgzrun
import random
WIDTH = 700
HEIGHT = 300
gap = WIDTH/4
bag = Actor("paperimg")
items = ["bottleimg","chipsimg"]
actors = []
def make_actor():
    for num in items:
        x = Actor(num)
        actors.append(x)
    actors.append(bag)
    random.shuffle(actors)
    for i in range(len(actors)):
        actors[i].x = gap*(i+1)
    for x in actors:
        animate(x,duration = 10,y = HEIGHT)
make_actor()
def draw():
    screen.blit("new_bg",(0,0))
    bag.draw()
    for actor in actors:
        actor.draw()



pgzrun.go()