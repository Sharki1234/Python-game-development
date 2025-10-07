import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])
bg = pygame.image.load("pygame/Rocket Simulation/Image20251003181525.png")
clock = pygame.time.Clock()
class Bird():
    def __init__(self,x,y):
        self.images = [pygame.image.load(f"pygame/Rocket Simulation/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x,self.y))
    def update(self):
        self.index = (self.index+1)%3
        self.image = self.images[self.index]
        self.y+=2
        self.x+=2
        if pygame.mouse.get_pressed()[0]:
            self.y-=6


    
bird = Bird(300,300)

while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(bird.image,(bird.x,bird.y))
    bird.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()