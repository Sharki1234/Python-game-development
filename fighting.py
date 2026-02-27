import pgzrun
from random import randint

WIDTH = 680
HEIGHT = 400
TITLE = "FIGHTER JET GAME"
score = 0
fighter_jet = Actor("fighter_jet")
bg = Actor("bg")
enemy_jet = Actor("fighter_jet2")
fighter_jet.pos=(250,380)
bg.pos=(340,200)
bullets = []
def draw():
    bg.draw()
    fighter_jet.draw()
    enemy_jet.draw()
    score_update()
    for b in bullets:
        b.draw()

def score_update():
    screen.draw.text(f"SCORE:{score}",(10,10),color = "red")

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=fighter_jet.x
        bullets[-1].y=fighter_jet.y-50

def update():
    global score,extra_enemy_added
    screen.clear()
    if keyboard.left:
        fighter_jet.x-=10
        if fighter_jet.x<25:
            fighter_jet.x=25
    if keyboard.right:
        fighter_jet.x+=10
        if fighter_jet.x>650:
            fighter_jet.x=650
    #move enemy
    enemy_jet.y+=5
    if enemy_jet.y>400:
        enemy_jet.y=0
        enemy_jet.x=randint(0,680)
    for b in bullets:
        b.y-=10
        if b.y<=0:
            bullets.remove(b)
        if enemy_jet.colliderect(b):
            score+=10
            bullets.remove(b)
            enemy_jet.y=0
            enemy_jet.x=randint(0,680)

            



           













































pgzrun.go()