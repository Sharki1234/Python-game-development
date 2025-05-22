import pgzrun
import random
import time
WIDTH = 500
HEIGHT =500
score = 0
message = " "
body = []

snake = Actor("red-star")
food = Actor("batteryimg")

def foodpos():
     x = random.randint(0,WIDTH)
     y = random.randint(0,HEIGHT)
     food.x = x
     food.y = y

foodpos()


def draw():
    screen.blit("bground",(0,0))
    snake.draw()
    food.draw()

    # message = (f"your score is: {score}")
    # screen.draw.text(message,center = (50,20),fontsize = 20)
    if coll() == True:
        part = Actor("red-star")
        x = snake.x
        y = snake.y
        part.x = x
        part.y = y
        part.draw()
    for b in body:
        b.draw()
   

def stop(body):
    if snake.x == WIDTH or snake.x == 0 or snake.y == HEIGHT or snake.y == 0:
        for i in range(len(body)):
            body[i].x = WIDTH*2
            body.y[i] = HEIGHT*2
            body[i] = []
    return False

def coll():
    global food
    if snake.colliderect(food):
        
            
        return True
        

def update():
    global score
    if keyboard.right:
        ani = animate(snake,duration = 10,x = WIDTH)
        for i in body:
            ani = animate(i,duration = 10,x = WIDTH)
        
    elif keyboard.left:
        ani = animate(snake,duration = 10,x = WIDTH-WIDTH)
        for i in body:
            ani = animate(i,duration = 10,x = WIDTH - WIDTH)
        
    elif keyboard.up:
        ani = animate(snake,duration = 10,y = HEIGHT - HEIGHT)
        for i in body:
            ani = animate(i,duration = 10,y = HEIGHT-HEIGHT)
        
    elif keyboard.down:
        ani = animate(snake,duration = 10,y = HEIGHT)
        for i in body:
            ani = animate(i,duration = 10,y = HEIGHT)
        

    gameover = stop(body)
    if not gameover:
        x = 0
    
            
            

    for i in range(len(body)-1,0,-1):
        x,y = body[i-1].x,body[i-1].y
        body[i].x = x
        body[i].y= y 



    
  






pgzrun.go()
