import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))

start = True

class Circle():
    def __init__(self,colour,center,radius):
        self.colour = colour
        self.radius = radius
        self.center = center
        self.scrn = screen
    def draw(self):
        pygame.draw.circle(self.scrn,self.colour,self.center,self.radius)
    def grow(self):
        self.radius +=10
        pygame.draw.circle(self.scrn,self.colour,self.center,self.radius)


radius = 40
while start:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            start = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tiny_circle = Circle((0,0,255),(250,250),radius)
            tiny_circle.draw()
        elif event.type == pygame.MOUSEBUTTONUP:
            radius+=20
        pygame.display.update()