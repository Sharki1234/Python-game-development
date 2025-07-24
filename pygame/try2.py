import pygame
import time
pygame.init()
CELL_SIZE = 20
CELL_HEIGHT = 20
CELL_WIDTH = 20
screen = pygame.display.set_mode((30*CELL_WIDTH,30*CELL_HEIGHT))


class Snake:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.direction = [0,1]
        self.snake = [[self.x*CELL_SIZE,self.y*CELL_SIZE]]
        self.rects = []
        self.new  = []
        
        
    def create_rect(self):
        for segment in self.snake:
            rect = pygame.Rect(segment[0],segment[1],self.width,self.height)
            self.rects.append(rect)
    def draw(self):
        self.rects = []
        self.create_rect()
        for rect in self.rects:
            pygame.draw.rect(screen,(0,255,0),rect)
    
    def move(self,rect):
        
        dx = self.snake[0][0]+(self.direction[0]*CELL_SIZE)
        dy = self.snake[0][1]+(self.direction[1]*CELL_SIZE)
        new = [dx,dy]
        self.snake.insert(0,new)
       
    def collide(self,rect):
        if self.rects[0].colliderect(rect):
            return True
        else:
            self.snake.pop()
    def up(self):
         if self.direction != (0,1):
            self.direction = (0,-1)
    def down(self):
        if self.direction != (0,-1):
            self.direction = (0,1)
        

    def left(self):
        if  self.direction != (1,0):
            self.direction = (-1,0)
    def right(self):
        if  self.direction != (-1,0):
            self.direction = (1,0)
    

        
        
        
        
        
    
class Food:
    def __init__(self,radius,x,y):
        self.radius = radius
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen,center=(self.x,self.y),radius = self.radius,color = (125,125,255))
    def invisa_rect(self):
        rect = pygame.Rect(self.x-self.radius,self.y-self.radius,self.radius*2,self.radius*2)
        return rect
            
    

snake = Snake(CELL_WIDTH,CELL_HEIGHT,6,12)
food = Food(10,20,20)
while True:
    screen.fill((200,255,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
            if event.key == pygame.K_UP:
                snake.up()
            if event.key == pygame.K_DOWN:
                snake.down()
            
            
    
    snake.move(food.invisa_rect())
    snake.draw()
    food.draw()
    
   
    time.sleep(0.1)
    pygame.display.update()