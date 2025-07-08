import pygame
import random
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
moving = True
move = [0,10]
while True:
    screen.blit(bee,(x,y))
    screen.blit(flower,(fx,fy))
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
                moving = True
            elif event.key == pygame.K_LEFT:
                moving = True
            elif event.key == pygame.K_UP:
                moving = True
            elif event.key == pygame.K_DOWN:
                moving = True
        if fx - x<10 and fx-x>-10:
            fx = random.randint(0,WIDTH) 
        elif fy - y<10 and fy-y>-10:
            fy = random.randint(0,WIDTH)       
        if not moving:
            x+=move[0]
            y+=move[1]
        screen.fill((122,255,122))
        screen.blit(bee,(x,y))
        screen.blit(flower,(fx,fy))
        pygame.display.update()

        
        
    

            
        