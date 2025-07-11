import pygame
import time
pygame.init()
screen = pygame.display.set_mode([1000,1000])
rocket = pygame.image.load("pygame\Rocket Simulation\character.png")
start = True
x = 250
y = 0
moving = True
keys = [False,False,False]
while start:
    screen.fill((125,255,125))
    screen.blit(rocket,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                  keys[0] = True
            if event.key == pygame.K_RIGHT:
                  keys[1] = True
            if event.key == pygame.K_UP:
                  keys[2] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                  keys[0] = False
            if event.key == pygame.K_RIGHT:
                  keys[1] = False
            if event.key == pygame.K_UP:
                  keys[2] = False
    if moving:
        y+=5
    if keys[0]:
         x-=5
    if keys[1]:
         x+=5
    if keys[2]:
         y-=10

    time.sleep(0.05) 
        
    pygame.display.update()