import pygame
import random
pygame.init()
screen = pygame.display.set_mode([500,500])
bg = pygame.image.load("pygame/images/new_bg.jpg")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bin = pygame.image.load("pygame/images/bagimg.png")
        self.rect = self.bin.get_rect()
        self.x = 10
        self.y = 10
        self.rect.x = self.x
        self.rect.y = self.y
    def left(self):
        self.x-=10

class Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame/images/bottleimg.png")
        self.bottle = self.image
        self.rect = self.bottle.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = random.randint(50,450)
        

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame/images/bagimg.png")
        self.bag = self.image
        self.rect = self.bag.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = random.randint(50,450)
        
bin = Bin
recyclable_list = pygame.sprite.Group()
non_recyclable_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

#all_list = pygame.sprite.Group()
for i in range(5):
    bottle = Recyclable()
    recyclable_list.add(bottle)
for i in range(5):
    bag = Non_recyclable()
    non_recyclable_list.add(bag)

all_sprites.add(recyclable_list,non_recyclable_list)
all_sprites.add(bin)
     
while True:
    screen.blit(bg,(0,0))
    all_sprites.update()
   
    all_sprites.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key() == pygame.K_LEFT:
                bin.left()
    pygame.display.update()