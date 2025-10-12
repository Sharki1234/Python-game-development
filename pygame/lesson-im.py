import pygame
import time
pygame.init()
screen = pygame.display.set_mode([500,500])
bg = pygame.image.load("pygame\Rocket Simulation\space.png")
gun_sound = pygame.mixer.Sound("pygame\Rocket Simulation\Gun+Silencer.mp3")
collision_sound = pygame.mixer.Sound("pygame\Rocket Simulation\Grenade+1.mp3")

class Rocket:
    def __init__(self,x,y,images,angle,direction,colour):
        self.x = x
        self.y = y
        self.images = images
        self.angle = angle
        self.move = 0
        self.direction = direction
        self.colour = colour
        self.score = 0
        self.lives = 3
        #.stop = True
        # self.b = Bullet(self.x,self.y,(0,0,255),direction)
        self.bullets = []
    def create_rocket(self):
        self.rocket = pygame.image.load(self.images)
        self.rocket = pygame.transform.scale(self.rocket,(50,50))
        self.rocket = pygame.transform.rotate(self.rocket,self.angle)
        return self.rocket
    def draw(self):
        screen.blit(self.create_rocket(),(self.x,self.y))
    def movement(self):
        #self.stop = False
        self.y+= self.move
    def up(self):
        self.move = -5
    def down(self):
        self.move = 5
    def stop(self):
        self.move = 0
    def bullet(self):
        self.b = Bullet(self.x,self.y,(0,0,255),self.direction)
        self.bullets.append(self.b.create())
        gun_sound.play()
    def draw_bullets(self):
        for rect in self.bullets[:]:
            
            pygame.draw.rect(screen,self.colour,rect)
            self.b.movement(self.y,rect)
            if rect.x<=0 or rect.x>=500:
                self.bullets.remove(rect)
        
            
    def invisa_rect(self):
        self.width,self.height = self.rocket.get_width(),self.rocket.get_height()
        self.invisa = pygame.Rect(self.x,self.y,self.width,self.height)
        return self.invisa
    def check_collision(self,r,otherbullets):
        
        for i in self.bullets[:]:
            if r.invisa_rect().colliderect(i):
                
                self.bullets.remove(i)
                self.score +=1
                collision_sound.play()
                r.lives-=1
      

        
    def scoreprint(self,left,top):
        font = pygame.font.SysFont("Arial",20)
        text = font.render(("score:"+str(self.score)),1,(0,0,0))
        screen.blit(text,(left,top))
    def livesprint(self,left,top):
        font = pygame.font.SysFont("Arial",20)
        text = font.render(("lives:"+str(self.lives)),1,(0,0,0))
        screen.blit(text,(left,top))
                
            

class Bullet:
    def __init__(self,x,y,colour,direction):
        self.colour = colour
        self.direction = direction
        self.x = x
        self.y = y
    def create(self):
        self.rect = pygame.Rect((self.x,self.y),(10,10))
        return self.rect
    
    def movement(self,y,rectangle):
        self.rectangle = rectangle
        self.rectangle.x+=self.direction
        self.y = y
    

    

        

rocket1 = Rocket(50,100,"pygame\Rocket Simulation\spaceship_red.png",90,5,(255,0,0))

rocket2 = Rocket(400,100,"pygame\Rocket Simulation\spaceship_yellow.png",270,-5,(255,255,0))

while True:
    screen.blit(bg,(0,0))
    rocket1.draw()
    rocket2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket1.up()
            elif event.key == pygame.K_RIGHT:
                rocket1.down()
            elif event.key == pygame.K_UP:
                rocket2.up()
            elif event.key == pygame.K_DOWN:
                rocket2.down()
            elif event.key == pygame.K_LSHIFT:
                rocket1.bullet()
            elif event.key == pygame.K_LALT:
                rocket2.bullet()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rocket1.stop()
            elif event.key == pygame.K_RIGHT:
                rocket1.stop()
            elif event.key == pygame.K_UP:
                rocket2.stop()
            elif event.key == pygame.K_DOWN:
                rocket2.stop()
    #pygame.
    rocket1.movement()
    rocket1.draw_bullets()
    rocket2.movement()
    rocket2.draw_bullets()
    rocket2.check_collision(rocket1,rocket1.bullets)
    rocket1.check_collision(rocket2,rocket2.bullets)
    
   
    rocket1.scoreprint(10,10)
    rocket2.scoreprint(440,10)
    rocket2.livesprint(440,30)
    rocket1.livesprint(10,30)

    
    pygame.display.update()
    time.sleep(0.005)