import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Birthday card")
bg = pygame.image.load("pygame/backgroundone.jpg")

font = pygame.font.SysFont("Arial",60)
text = font.render("Happy Birthday",1,(0,0,0))
while (True):
    screen.blit(bg,(0,0))
    screen.blit(text,(200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
pygame.quit()      