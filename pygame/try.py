import pygame
import random
import time
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((122,255,122))
bee = pygame.image.load("pygame/Rocket Simulation/bee.png")
flower = pygame.image.load("pygame\Rocket Simulation/flower.png")
x = 0
y = 0
fx = random.randint(0,WIDTH)
fy = random.randint(0,HEIGHT)
bwidth,bheight = bee.get_width(),bee.get_height()
fwidth,fheight = flower.get_width(),flower.get_height()
moving = True
move = [0,10]

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = False
                move[0] = 10
                move[1] = 0
            elif event.key == pygame.K_LEFT:
                moving = False
                move[0] = -10
                move[1] = 0
            elif event.key == pygame.K_UP:
                moving = False
                move[0] = 0
                move[1] = -10
            elif event.key == pygame.K_DOWN:
                
                moving = False
                move[0] = 0
                move[1] = 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move[0] = 0
                move[1] = 0
            elif event.key == pygame.K_LEFT:
                move[0] = 0
                move[1] = 0
            elif event.key == pygame.K_UP:
                move[0] = 0
                move[1] = 0
            elif event.key == pygame.K_DOWN:
                move[0] = 0
                move[1] = 0

           
    
    if not moving:
        x+=move[0]
        y+=move[1]
    screen.fill((122,255,122))
    brect = pygame.Rect((x,y),(bwidth,bheight))
    frect = pygame.Rect((fx,fy),(fwidth,fheight))
    if brect.colliderect(frect):
        fx = random.randint(20,WIDTH-20)
        fy = random.randint(20,HEIGHT-20)
    screen.blit(bee,(x,y))
    screen.blit(flower,(fx,fy))
    time.sleep(0.05)
    pygame.display.update()
