import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode([500,500])
#bg = pygame.image.load("pygame/images/new_bg.jpg")
score = 0

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame/images/paperimg.png")
        self.bin = self.image
        self.rect = self.bin.get_rect()
        self.direction = [0,0]
        self.rect.x = 250
        self.rect.y = 250
    def move(self):
        self.rect.x+=self.direction[0]
        self.rect.y+=self.direction[1]
    def left(self):
        self.direction[0] = -2
        self.direction[1] = 0
    def right(self):
        self.direction[0] = 2
        self.direction[1] = 0
    def down(self):
        self.direction[0] = 0
        self.direction[1] = 2
    def up(self):
        self.direction[0] = 0
        self.direction[1] = -2
    def stop(self):
        self.direction[0] = 0
        self.direction[1] =0
    

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
        self.bag = pygame.image.load("pygame/images/bagimg.png")
        #self.bag = self.image
        self.rect = self.bag.get_rect()
        self.rect.x = random.randint(50,450)
        self.rect.y = random.randint(50,450)
        
bin = Bin()
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
            if event.key == pygame.K_LEFT:
                bin.left()
            if event.key == pygame.K_RIGHT:
                bin.right()
            if event.key == pygame.K_DOWN:
                bin.down()
            if event.key == pygame.K_UP:
                bin.up()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bin.stop()
            if event.key == pygame.K_RIGHT:
                bin.stop()
            if event.key == pygame.K_DOWN:
                bin.stop()
            if event.key == pygame.K_UP:
                bin.stop()
        
        collided = pygame.sprite.spritecollide(bin,recyclable_list,True)
        score+=len(collided)
        
    font = pygame.font.SysFont("Arial",20)
    text = font.render(("score:"+str(score)),1,(0,0,0))
    screen.blit(text,(20,20))
    bin.move()
    time.sleep(0.004)
    pygame.display.update()