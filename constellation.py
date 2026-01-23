import pgzrun
from random import randint
from time import time

WIDTH = 500
HEIGHT = 500
TITLE = "STAR GAME-CONNECTING STARS"

stars = []#this will store all the satelites created
lines = []#this will store all the lines that are joining the star
next_star = 0#this number tells us what the next star to be clicked is
start_time  = 0#records the time started game
end_time = 0#records the time ended game
total_time = 0#end_time - start_time
no_stars = 10#number of stars in the game

def create_stars():
    global start_time
    for i in range(1,no_stars+1):
        star = Actor("star")
        star.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        stars.append(star)
    start_time=time()    

def draw():
    global total_time
    screen.blit("bg",(0,0))#Creates background for game
    number = 1#Start number for stars
    for star in stars:#this loop checks all stars in the list of stars
        screen.draw.text(str(number),(star.pos[0]+10,star.pos[1]+30))#writes the number on each star
        star.draw()
        number+=1
    for line in lines: 
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_star<no_stars:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 50)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 50)
        screen.draw.text("GAME OVER,YOU HAVE WON",(150,10),fontsize = 30)
def update():
    pass
def on_mouse_down(pos):#event to click with the position
    global next_star
    global lines
    if next_star<no_stars:
        if stars[next_star].collidepoint(pos):
            if next_star:
                lines.append((stars[next_star-1].pos,stars[next_star].pos))
            next_star += 1 
        else:
            lines = []
            next_star = 0
create_stars()
pgzrun.go()