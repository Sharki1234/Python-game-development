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
    for b in body:
        b.draw()
   

def stop(body):
    if snake.x == WIDTH or snake.x == 0 or snake.y == HEIGHT or snake.y == 0:
        for i in range(len(body)):
            body.x = WIDTH*2
            body.y = HEIGHT*2
            body = []
    return False

def update():
    global score
    if keyboard.left:
        ani = animate(snake,duration = 10,x = WIDTH)
        for i in 
        anib = animate(body,duration = 10,x = WIDTH)
    elif keyboard.right:
        ani = animate(snake,duration = 10,x = WIDTH)
    elif keyboard.up:
        ani = animate(snake,duration = 10,y = HEIGHT)
    elif keyboard.down:
        ani = animate(snake,duration = 10,y = HEIGHT)

    gameover = stop(body)
    if not gameover:
        print("hi")
    if snake.colliderect(food):
        print("hello")
        
        score+=1
            
        foodpos()
        part = Actor("red-star")
        x = snake.x
        y = snake.y
        part.x = x
        part.y = y
        body.append(part)
            
            

    for i in range(len(body)-1,0,-1):
        x,y = body[i-1].x,body[i-1].y
        body[i].x = x
        body[i].y= y 



    
  






pgzrun.go()
