import pgzrun
import random
WIDTH = 500
HEIGHT = 410
gap = 10
full = [] 
recs = []
level = 0

def get_questions():
    file = open("23.05.2025\practice.txt","r")
    
    data = file.readlines()

    print(data)
    for datum in data:
        q = datum.split(",")
        print(q)
        question = q[0]
        options = []
        for i in range(1,5):
            options.append(q[i])
        print(options)
        answer = int(q[5])
        dict = {
            "question":question,
            "options":options,
            "answer":answer-1
        }
        full.append(dict)
    random.shuffle(full)

    print(full)
    file.close()
get_questions()

def draw():
    x = (WIDTH - (gap*3))/2
    y = (HEIGHT - (gap*4))/3
    p = gap + (x/2)
    n = (y+(gap*2))+(y/2)
    screen.fill(color = (150,238,137))  
    rect = Rect((0,0),(x,y))
    rect.center = (p,n)
    screen.draw.filled_rect(rect,(8,84,47))#drawing teh rectangles

    rect2 = Rect((0,0),(x,y))
    rect2.center = (WIDTH-p,n)
    screen.draw.filled_rect(rect2,(8,84,47))

    rect3 = Rect((0,0),(x,y))
    rect3.center =(WIDTH-p,n+(y)+gap)
    screen.draw.filled_rect(rect3,(8,84,47))

    rect4 = Rect((0,0),(x,y))
    rect4.center = (p,n+(y)+gap)
    screen.draw.filled_rect(rect4,(8,84,47))

    qbox = Rect((0,0),((2*x)+gap,y))
    qbox.center = ((gap*1.5)+x,gap+(y/2))
    screen.draw.filled_rect(qbox,(1,45,33))

    recs.append(rect)#adding to list
    recs.append(rect2)
    recs.append(rect3)
    recs.append(rect4)
    screen.draw.text((full[level]["question"]),(gap+10,gap+(y/2)),fontsize = 20)#putting question into teh box
    screen.draw.text(full[level]["options"][0],((gap+10),n),fontsize=20)
    screen.draw.text(full[level]["options"][1],(WIDTH-p,n),fontsize=20)
    screen.draw.text(full[level]["options"][2],(WIDTH-p,n+(y)+gap),fontsize=20)
    screen.draw.text(full[level]["options"][3],(p,n+(y)+gap),fontsize=20)
    #printing options

def on_mouse_down(pos):
    global level,full
    for i in range(len(recs)):
        if recs[i].collidepoint(pos):
            if i == full[level]["answer"] and level<=len(full):
                level+=1#if the index of the rectangle that you have clicked is equal to teh index of the answer 
                #you will move to teh next level
            if level>len(full):
                full = []
        

pgzrun.go()
