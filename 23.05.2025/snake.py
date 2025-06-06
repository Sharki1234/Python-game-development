import pgzrun
import time
import random
WIDTH = 400
HEIGHT = 400


last_u = 0
CELL_SIZE = 20
CELL_WIDTH = 20
CELL_HEIGHT = 20
snake = [[6,12]]
direction = (0,0)
food = (16,4)

def draw():
    screen.clear()
    screen.fill(color = "white")
    for segment in snake:
        rect = Rect((segment[0]*CELL_SIZE,segment[1]*CELL_SIZE),(CELL_SIZE,CELL_SIZE))
        screen.draw.filled_rect(rect,color = "green")
    screen.draw.filled_circle((food[0]*CELL_SIZE,food[1]*CELL_SIZE),10,color = "red")

def on_key_down(key):
    global direction
    if key == keys.UP and direction != (0,1):
        direction = (0,-1)
    elif key == keys.DOWN and direction != (0,-1):
        direction = (0,1)
    elif key == keys.LEFT and direction != (1,0):
        direction = (-1,0)
    elif key == keys.RIGHT and direction != (-1,0):
        direction = (1,0)

def move():
    global food
    dx = snake[0][0]+direction[0]
    dy = snake[0][1]+direction[1]
    new = [dx,dy]
    snake.insert(0,new)
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = random.randint(1,19),random.randint(1,19)
    else:
        snake.pop()


def update():
    global last_u
    current_time = time.time()
    if current_time - last_u>0.2:
        move()
        last_u = current_time
        
pgzrun.go()