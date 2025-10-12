import pygame
import random
pygame.init()
screen = pygame.display.set_mode([600,600])
bg = pygame.image.load("pygame/Rocket Simulation/Image20251003181525.png")
ground = pygame.image.load("pygame\Rocket Simulation\ground.png")
clock = pygame.time.Clock()
class Bird():
    def __init__(self,x,y):
        self.images = [pygame.image.load(f"pygame/Rocket Simulation/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.velocity = 0
    def update(self):
        self.index = (self.index+1)%3
        self.image = self.images[self.index]
        self.velocity+=0.2
        self.rect.y+=self.velocity
        self.rect.x+=2
        if pygame.mouse.get_pressed()[0]:
            self.velocity = -5
            self.rect.y+=self.velocity
 


class Pipe(pygame.sprite.Sprite):
    def __init__(self,invert):
        super().__init__()
        self.image = pygame.image.load("pygame\Rocket Simulation\pipe.png")
        self.pipe = self.image
        self.rect = self.pipe.get_rect()
        self.y = 300
        self.x = 300
        self.invert = invert
        self.pipe_gap = 50
        
    def update(self):
        self.x -= 10
        
        if self.invert == True:
            self.rect.topleft = (self.x,self.y+self.pipe_gap)
        else:
            
            self.rect.bottomleft = (self.x,self.y-self.pipe_gap)
        #self.rect.topleft = (self.x,random.randint(0,450))

    
bird = Bird(300,300)
pipe_group = pygame.sprite.Group()
pipe = Pipe(True)
pipe2 = Pipe(False)
pipe_group.add(pipe)
pipe_group.add(pipe2)


ground_x = 0
while True:
    clock.tick(10)
    screen.blit(bg,(0,0))
    
    screen.blit(bird.image,(bird.rect))
    bird.update()
    pipe_group.update()
    pipe_group.draw(screen)
    screen.blit(ground,(ground_x,450))
    screen.blit(ground,(800+ground_x,450))
    ground_x-=5
    if ground_x == -800:
        ground_x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
