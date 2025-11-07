import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Calc:
    def __init__(self):
        self.buttons = []
        self.board()
        self.button_values = [[7,8,9,"/"],[4,5,6,"X"],[3,2,1,"-"],["+",0,"=","AC"]]
        self.equation = []
        self.num = []
    def board(self):
        gap = 50
        self.answerboard = pygame.Rect((gap),(gap),WIDTH-(gap*2),(gap*3))
        buttonscreen_width = gap*10
        buttonscreen_height = gap*6
        button_width = (buttonscreen_width-(gap*3))/4
        button_height = (buttonscreen_height-((gap/2)*3))/4
        for n in range (4):
            button_row = []
            for i in range(4):
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

        for i in range(len(self.buttons)):
            for n in range(len(self.buttons[i])):
                font = pygame.font.SysFont("Times New Roman",20)
                t = self.button_values[i][n]
                text = font.render(str(t),1,(0,0,0))
                screen.blit(text,(self.buttons[i][n].center))
    def click(self):
        pos = pygame.mouse.get_pos()
        for i in range(len(self.buttons)):
            for n in range(len(self.buttons[i])):
                if self.buttons[i][n].collidepoint(pos):
                    self.equation.append(self.button_values[i][n])
                    if self.equation[-1] == "+" or self.equation[-1] =="/" or self.equation[-1] =="X" or self.equation[-1] == "-" or self.equation[-1] =="=":
                        self.numb = 0
                        for i in range(len(self.equation)):
                            self.numb += self.equation[i]*(10**(len(self.equation)-i))
                        self.num.append(self.numb)
                        self.numb = 0
                        print(self.num)
           
calc = Calc()  
while True:
    screen.fill((165,240,154))
    calc.board_draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            calc.click()
    pygame.display.update()