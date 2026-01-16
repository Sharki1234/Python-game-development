import pgzrun
from random import randint
from time import time

WIDTH = 500
HEIGHT = 500
TITLE = "SATELLITE GAME-CONNECTING SATELLITES"

satellites = []#this will store all the satelites created
lines = []#this will store all the lines that are joining the satellite
next_satellite = 0#this number tells us what the next satellite to be clicked is
start_time  = 0#records the time started game
end_time = 0#records the time ended game
total_time = 0#end_time - start_time
no_satellites = 10#number of satellites in the game

def create_satellites():
    global start_time
    for i in range(1,no_satellites+1):
        satellite = Actor("satelite")
        satellite.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        satellites.append(satellite)
    start_time=time()    

def draw():
    global total_time
    screen.blit("bg",(0,0))#Creates background for game
    number = 1#Start number for satellites
    for satellite in satellites:#this loop checks all satellites in the list of satellites
        screen.draw.text(str(number),(satellite.pos[0]+10,satellite.pos[1]+20))#writes the number on each satellite
        satellite.draw()
        number+=1
    for line in lines: 
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_satellite<no_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 50)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 50)
        screen.draw.text("GAME OVER,YOU HAVE WON",(150,10),fontsize = 30)
def update():
    pass
def on_mouse_down(pos):#event to click with the position
    global next_satellite
    global lines
    if next_satellite<no_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite += 1 
        else:
            lines = []
            next_satellite = 0
create_satellites()
pgzrun.go()