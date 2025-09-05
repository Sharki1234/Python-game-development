import pygame
import time
pygame.init()
screen = pygame.display.set_mode([500,500])
width = 250
rect = pygame.Rect((250,250),(width,250))
x = 255
while True:
    pygame.draw.rect(screen,(x,125,125),rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                x = 0
    pygame.display.update()