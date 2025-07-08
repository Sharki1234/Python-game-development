import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Birthday card")
bg = pygame.image.load("pygame/backgroundone.jpg")
bg2 = pygame.image.load("pygame/backgroundtwo.jpg")
bg3 = pygame.image.load("pygame/backgroundthree.jpg")
l = 0
font = pygame.font.SysFont("Arial",60)
text = font.render("Happy Birthday",1,(0,0,0))
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if l == 0:
                screen.blit(bg,(0,0))
                screen.blit(text,(140,200))
            elif l == 1:
                text = " "
                screen.blit(bg2,(0,0))
            elif l == 2:
                screen.blit(bg3,(0,0))
        elif event.type  == pygame.MOUSEBUTTONUP:
            l+=1
    pygame.display.update()
pygame.quit()      