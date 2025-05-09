import pgzrun
import random
WIDTH = 500
HEIGHT = 400
stars = ["green-star","orange-star","red-star","purple-star"]
actors = []
selected = []
animation = []
num = 1
game_over = False

def make_actors():
    for i in range(num):
        selected.append(random.choice(stars))
    selected.append("blue-star")
    random.shuffle(selected)   
    for s in selected:
        actors.append(Actor(s))
    gap = WIDTH/(num+2) 
    for i in range(len(actors)):
         actors[i].x = gap*(i+1)
    for m in actors:
        y = animate(m,duration = 10,y = HEIGHT)
        animation.append(y)
    
make_actors()

def draw():
    screen.blit("space",(0,0))
    #blue.draw()
    for item in actors:
        item.draw()
    if game_over:
        screen.draw.text("GAME OVER",fontsize = 100,center = (250,100),color = "white")

def on_mouse_down(pos):
    global actors,selected,num,animation,game_over
    for i in range(num+1):
        if actors[i].collidepoint(pos):
            if  selected[i] == "blue-star":
                num+=1
                actors = []
                selected = []
                animation = []
                make_actors()
            else:
                for x in range(num+1):
                    if animation[x].running:
                        animation[x].stop()
                game_over = True



pgzrun.go()

