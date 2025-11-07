import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])
green = (125,255,125)
red = (255,125,125)
player_col = green

#kind of tic tac toe
class Recs:
    def __init__(self,width,hieght):
        self.width = width#screen width
        self.height = hieght#screen height
        self.rect_list = []
        self.user =[]
        self.create_recs()
    def create_recs(self):
        #create the recs by rows and use 2d list to store,then check if in order
        #for l in range(3):
        for n in range(3):#create rows
            self.rect = []
            self.u = []
            for i in range(3):
                rec = pygame.Rect((self.width/3*i),(self.height/3*n),self.width/3-10,self.height/3-10)
                self.rect.append(rec)
                self.u.append((255,255,255))
            self.rect_list.append(self.rect)
            self.user.append(self.u)
            
    def draw(self):
        
        for i in range(len(self.rect_list)):
            for n in range(len(self.rect_list[i])):
                pygame.draw.rect(screen,self.user[i][n],self.rect_list[i][n])
    def change(self,colour):
        pos = pygame.mouse.get_pos()
        for n in range(len(self.rect_list)):
            for i in range(len(self.rect_list[n])):
                if self.rect_list[n][i].collidepoint(pos):
                    self.user[n][i] = colour
    def check(self):
        for i in range(3):
            if self.user[i][1] == self.user[i][0] and self.user[i][1] == self.user[i][2] and self.user[i][1] != (255,255,255):
                print("winner")
            if self.user[1][1] == self.user[0][0] and self.user[2][2] == self.user[0][0]:
                print("winner")
            if self.user[1][1] == self.user[2][0] and self.user[0][2] == self.user[2][0]:
                print("winner")
            for n in range(3):
                if self.user[i][n] == self.user[i+1][n] and self.user[i+2][n] == self.user[i+1][n] and self.user[i][n] != (255,255,255):
                    print("winner")
            
   
        
recs = Recs(600,600)
print(recs.create_recs())
        
running = True
while running:
    screen.fill((0, 0, 0))  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            recs.change(player_col)
            recs.check()
            if player_col == green:
                player_col = red
            else: 
                player_col = green
    recs.draw()
    
    pygame.display.update()
pygame.quit()