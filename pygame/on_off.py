import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
bulb = pygame.image.load("pygame\BulbOn.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(bulb,(0,0))
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
    pygame.display.update()
