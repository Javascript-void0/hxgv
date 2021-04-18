# Keyboard import, use keyboard
# "Base Video Game"

from tkinter import Tk, Canvas, TclError
from time import sleep
from random import randint

window = Tk()

window.title("Animation")
cvs = Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball = cvs.create_oval(50,50,100,100,outline="red", fill="yellow")

bullet = []

enemy = []
enemy_spd = []

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def generate_bullet():
    x,y = get_pos(ball)
    new_bullet = cvs.create_oval(x-4, y-4, x+4, y+4, outline="red", fill="red")
    bullet.append(new_bullet)

def update_bullet():
    for i in range(len(bullet)):
        cvs.move(bullet[i], 2, 0)

def generate_enemy():
    x = 1200
    y = randint(0,800)
    r = randint(20,50)
    new_enemy = cvs.create_oval(x-r, y-r, x+r, y+r, outline="red", fill="yellow")
    enemy.append(new_enemy)
    enemy_spd.append(randint(2,6))

def update_enemy():
    for i in range(len(enemy)):
        cvs.move(enemy[i], -enemy_spd[i], 0)

def key_press(event):
    print(event.keysym)    
    if event.keysym=="Up":
        cvs.move(ball, 0, -5)
    if event.keysym=="Down":
        cvs.move(ball, 0, 5)
    if event.keysym=="Left":
        cvs.move(ball, -5, 0)
    if event.keysym=="Right":
        cvs.move(ball, 5, 0)
    if event.keysym=="space":
        generate_bullet()
    
def left_click(event):
    print(event.x, event.y)
    cvs.coords(ball, event.x-25, event.y-25, event.x+25, event.y+25)

cvs.bind_all('<Key>', key_press)
cvs.bind_all('<Button-1>', left_click)

while True:
    sleep(0.005)
    try:
        window.update()
        update_bullet()
        generate_enemy()
        update_enemy()
    except TclError:
        break