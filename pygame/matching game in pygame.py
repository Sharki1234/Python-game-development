import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
x = WIDTH/2
y = HEIGHT/3
recs = []


for i in range(3):
    for j in range(3):
       
        rect = pygame.Rect((x,y),(x/2+(x*i),y/2+(y*j)))

        recs.append(rect)
