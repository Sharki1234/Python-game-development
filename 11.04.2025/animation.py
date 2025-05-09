import pgzrun
import random
WIDTH = 700
HEIGHT = 300
level = 1
items = ["bottleimg","chipsimg","batteryimg","bagimg"]
selected_items = []
actors = []
over = False
animation = []
def make_actor():
    gap = WIDTH/(level+2)
    for i in range(level):
        add = random.choice(items)
        selected_items.append(add)
    selected_items.append("paperimg")
    random.shuffle(selected_items)
    for num in selected_items:
        x = Actor(num)
        actors.append(x)

    
    for i in range(len(actors)):
        actors[i].x = gap*(i+1)
    for x in actors:
        ani = animate(x,duration = 10,y = HEIGHT)
        animation.append(ani)
make_actor()
def draw():
    screen.blit("new_bg",(0,0))
    #bag.draw()
    for actor in actors:
        actor.draw()
    if over:
        screen.draw.text("GAME OVER",fontsize = 20,center = (50,50),color = "red")

def game_over():
    for i in range(level+1):
        if animation[i].running:
            animation[i].stop()
        


def on_mouse_down(pos):
    global level,selected_items,actors,animation,over

    for i in range(level+1):
        if actors[i].collidepoint(pos):
            if selected_items[i] == "paperimg":
                level+=1
                selected_items = []
                actors = []
                animation = []
                make_actor()
            else:
                game_over()
                over = True
                


pgzrun.go()