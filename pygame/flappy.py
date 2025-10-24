import pygame
import random
pygame.init()
screen = pygame.display.set_mode([600,600])
bg = pygame.image.load("pygame/Rocket Simulation/Image20251003181525.png")
ground = pygame.image.load("pygame\Rocket Simulation\ground.png")
clock = pygame.time.Clock()
score = 0
class Bird():
    def __init__(self,x,y):
        self.images = [pygame.image.load(f"pygame/Rocket Simulation/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.velocity = 0
        self.change = 0.2
        self.minus = -5
    def update(self):
        self.index = (self.index+1)%3
        self.image = self.images[self.index]
        self.velocity+=self.change
        self.rect.y+=self.velocity
        #self.rect.x+=2
        if pygame.mouse.get_pressed()[0]:
            self.velocity = self.minus
            #self.rect.y+=self.velocity
    def gameover(self):
        self.velocity = 0
        self.change = 0
        self.minus = 0
        self.index = 0
        self.rect.y = 300
 


class Pipe(pygame.sprite.Sprite):
    def __init__(self,invert,y):
        super().__init__()
        self.image = pygame.image.load("pygame\Rocket Simulation\pipe.png")
        self.pipe = self.image
        self.rect = self.pipe.get_rect()
        self.y = y
        self.x = 600
        self.passed = False
        self.invert = invert
        self.pipe_gap = 50

        if self.invert == True:
            self.rect.topleft = (self.x,self.y+self.pipe_gap)
        else:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (self.x,self.y-self.pipe_gap)
        
    def update(self):
        self.rect.x -= 10
        if self.rect.x == 0:
            self.kill()
        
       
        #self.rect.topleft = (self.x,random.randint(0,450))

    
bird = Bird(300,300)
pipe_group = pygame.sprite.Group()
prev_time = pygame.time.get_ticks()

scroll = 5
ground_x = 0
gameover = True
while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    
    screen.blit(bird.image,(bird.rect))
    
    ground_x-=scroll
    if ground_x == -800:
        ground_x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    current = pygame.time.get_ticks()

    if current-prev_time>1500 and gameover == True:
        y = random.randint(150,300)
        pipe = Pipe(True,y)
        pipe2 = Pipe(False,y)
        pipe_group.add(pipe)
        pipe_group.add(pipe2)
        prev_time = current
    
    bird.update()
    pipe_group.update()
    pipe_group.draw(screen)
    screen.blit(ground,(ground_x,450))
    screen.blit(ground,(800+ground_x,450))
    for pipe in pipe_group:
        if pipe.rect.right < bird.rect.left and pipe.passed == False and pipe.rect.bottom>=600:
            pipe.passed = True
            score+=1
            print(score)

    if pygame.sprite.spritecollide(bird,pipe_group,False):
        pipe_group.empty()
        bird.gameover()
        scroll = 0
        gameover = False

    pygame.display.update()
