import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))

x=250
y = 250
start = True

class Circle():
    def __init__(self,colour,radius):
        self.colour = colour
        self.radius = radius
        #self.center = center
        self.scrn = screen
    def draw(self,center):
        pygame.draw.circle(self.scrn,self.colour,center,self.radius)
        return center
    def grow(self,center):
        self.radius +=10
        pygame.draw.circle(self.scrn,self.colour,center,self.radius)

tiny_circle = Circle((0,0,255),1)
medium_circle = Circle((0,255,0),11)
big_circle = Circle((255,0,0),21)

while start:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            start = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:

            
            
            big_circle.draw(pygame.mouse.get_pos())
            medium_circle.draw(pygame.mouse.get_pos())
            tiny_circle.draw(pygame.mouse.get_pos())
            
            
            
        elif event.type == pygame.MOUSEBUTTONUP:
            
            big_circle.grow(pygame.mouse.get_pos())
            medium_circle.grow(pygame.mouse.get_pos())
            tiny_circle.grow(pygame.mouse.get_pos())
            
            
            
        pygame.display.update()