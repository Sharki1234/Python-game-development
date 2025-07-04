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

tiny_circle = Circle((0,0,255),(250,250),40)
medium_circle = Circle((0,255,0),(250,250),40+20)
big_circle = Circle((255,0,0),(250,250),40+40)

while start:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            start = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            
            
            big_circle.draw()
            medium_circle.draw()
            tiny_circle.draw()
            
            
            
        elif event.type == pygame.MOUSEBUTTONUP:
            
            big_circle.grow()
            medium_circle.grow()
            tiny_circle.grow()
            
            
            
        pygame.display.update()