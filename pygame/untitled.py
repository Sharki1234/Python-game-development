import pygame
import time
pygame.init()
screen = pygame.display.set_mode([500,500])
move = 0
direction = [5,5]
class Paddle:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def create_rect(self):
        rect = pygame.Rect((self.x,self.y),(self.width,self.height))
        return rect
    def draw(self):
        rect = self.create_rect()
        pygame.draw.rect(screen,(255,125,125),rect)
    def movement(self):
        self.x += move
   

# rect = pygame.Rect((250,400),(100,30))
r = Paddle(250,400,100,30)
while True:
    #pygame.draw.rect(screen,(255,125,125),rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move = -5
            if event.key == pygame.K_RIGHT:
                move = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move = 0
            if event.key == pygame.K_RIGHT:
                move = 0
    screen.fill((0,0,0))
    r.draw()
    r.movement()
    time.sleep(0.05)

    pygame.display.update()
