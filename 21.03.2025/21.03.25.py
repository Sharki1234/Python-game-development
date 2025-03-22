import pgzrun
import random

WIDTH = 500
HEIGHT = 500

sprite = Actor('alien')
sprite2 = Actor('flower')
message = ""
def draw():
    screen.clear()
    screen.fill(color = (128,0,0))
    sprite.draw()
    sprite2.draw()
    screen.draw.text(message,center = (20,20),fontsize = 20)

def on_mouse_down(pos):
    global message
    if sprite.collidepoint(pos):
        sprite.x = random.randint(0,500)
        sprite.y = random.randint(0,500)
        message = "well done you hit the alien"
    print(pos)

def update():
    if  keyboard.left:
       sprite.x-=10
    elif  keyboard.right:
       sprite.x+=10
    elif  keyboard.up:
       sprite.y-=10
    elif  keyboard.down:
       sprite.y+=10
    
    if sprite.colliderect(sprite2):
        sprite2.x = random.randint(0,500)
        sprite2.y = random.randint(0,500)
pgzrun.go()