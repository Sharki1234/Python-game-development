import pgzrun
import random
WIDTH = 500
HEIGHT = 400
blue = Actor("blue-star")
stars = ["green-star","orange-star","red-star","purple-star"]
actors = []
selected = []
gap = WIDTH/(len(stars)+2)
num = 3
def make_actors():
    actors.append(blue)
    for i in range(len(stars)):
        actors.append(Actor(stars[i]))
    random.shuffle(actors)    
     
    for i in range(len(actors)):
         actors[i].x = gap*(i+1)
    actors.pop(4)
    for m in actors:
        animate(m,duration = 10,y = HEIGHT)
    
    animate(blue,duration = 10,y = HEIGHT)

def select_actors():
    for i in range(num+1):
        selected.append(random.choice(actors))
    selected.append(blue)
    for x in range(len(selected)):  
        selected[x].x = (((WIDTH/len(selected))+2)*(x+1))
    

make_actors()
select_actors()

def draw():
    screen.blit("space",(0,0))
    #blue.draw()
    for item in selected:
        item.draw()

pgzrun.go()

