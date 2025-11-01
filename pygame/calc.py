import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Calc:
    def __init__(self):
        self.buttons = []
        self.board()
      
    def board(self):
        gap = 50
        self.answerboard = pygame.Rect((gap),(gap),WIDTH-(gap*2),(gap*3))
        buttonscreen_width = gap*10
        buttonscreen_height = gap*6
        buttonscreen = pygame.Rect(gap,gap*5,buttonscreen_width,buttonscreen_height)
        button_width = (buttonscreen_width-(gap*3))/4
        button_height = (buttonscreen_height-((gap/2)*3))/4
        for n in range (4):
            button_row = []
            for i in range(4):
                #left =  gap + ((WIDTH - (gap * 5)) / 4 + gap) * i
                button_left = (button_width*i)+(gap*(i+1))
                button_top = (button_height*n)+((gap/2)*(n+1))+(gap*4)
                button = pygame.Rect(button_left,button_top,button_width,button_height)
                button_row.append(button)
            self.buttons.append(button_row)
    def board_draw(self):
        for button_row in self.buttons:
            for button in button_row:
                pygame.draw.rect(screen,(17,130,59),button,0,4)
        pygame.draw.rect(screen,(72,191,83),self.answerboard,0,4)
calc = Calc()  
while True:
    screen.fill((165,240,154))
    calc.board_draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()