import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
bg = pygame.image.load("pygame/images/new_bg.jpg")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bin = pygame.image.load("pygame\images\bagimg.png")
        self.bin_rect = self.bin.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bottle = pygame.image.load("pygame/images/bottleimg.png")
        self.bottle_rect = self.bottle.get_rect()

recyclable_list = pygame.sprite.Group()
for i in range(5):
    bottle = Recyclable()     
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()