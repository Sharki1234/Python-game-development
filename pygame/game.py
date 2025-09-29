import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])

#kind of tic tac toe
class Recs:
    def __init__(self,width,hieght):
        self.width = width#screen width
        self.height = hieght#screen height
        self.rect_list = []
        self.user =[]
    def create_recs(self):
        #create the recs by rows and use 2d list to store,then check if in order
        for l in range(3):
            for n in range(3):#create rows
                self.rect = []
                for i in range(3):
                    rec = pygame.Rect((self.width/3*i),(self.height/3*n),self.width/3-10,self.height/3-10)
                    self.rect.append(rec)
                    self.user.append((255,255,255))
                self.rect_list.append(self.rect)
            return self.rect_list
    def draw(self):
        for l in self.create_recs[::]:
            for r in l:
                for i in self.user:
                    pygame.draw.rect(screen,i,r)
    #def change():

    
recs = Recs(600,600)
print(recs.create_recs())
        

while True:
    recs.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()