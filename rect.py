import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    x = 20
    y = 20
    z = 0
    p=255
   
    while x !=250 and y != 250:
        x+=10
        y+=10
        # rect = Rect((0,0),(x,y))
        # rect.center = 250,250
        # screen.draw.rect(rect,(255,p,z))
        screen.draw.circle((250,250),x,(255,p,z))
        z+=10
        p-=10

pgzrun.go()