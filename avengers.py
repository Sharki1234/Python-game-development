import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 400
TITLE = "U RATED EASY INFINITY WAR GAUNTLET CATCHING GAME"

score=0

iron_man = Actor("tony_stark")
iron_man.pos=(300,360)

thanos = Actor("thanos")
thanos.pos=(randint(0,500),65)

bg = Actor("bg")
bg.pos=(300,265)

infinity_gauntlet = Actor("infinity_gauntlet")
infinity_gauntlet.pos=(randint(0,500),65)

def draw():
    bg.draw()
    iron_man.draw()
    thanos.draw()
    infinity_gauntlet.draw()
    screen.draw.text("SCORE:{}".format(score),(5,5))

def update():
    global score
    if keyboard.left:
        iron_man.x=iron_man.x-10
        if iron_man.x<=0:
            iron_man.x=0
    if keyboard.right:
        #move iron man
        iron_man.x=iron_man.x+10 
        if iron_man.x>=500:
            iron_man.x=500   
    #move the gauntlet
    infinity_gauntlet.y+=6.5
    if infinity_gauntlet.y>400:
      infinity_gauntlet.y=0
      infinity_gauntlet.x=randint(0,500)
    #move thanos         
    thanos.y+=6.5
    if thanos.y>400:
        thanos.y=0
        thanos.x=randint(0,500) 
    #collision
    if iron_man.distance_to(thanos)<50:
        thanos.y=65
        thanos.x=randint(0,500)
        #if thanos collides with iron man,10 points are deducted
        score-=10
    if iron_man.distance_to(infinity_gauntlet)<50:
        infinity_gauntlet.y=65
        infinity_gauntlet.x=randint(0,500)
        #if infinity gauntlet collides with iron man,10 points are added
        score+=10
pgzrun.go()