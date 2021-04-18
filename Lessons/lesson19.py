# Snow Animation

from tkinter import Tk, Canvas, TclError
from time import sleep
from random import randint

window=Tk()

window.title("Snow")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball=cvs.create_oval(50,50,100,100,outline="red", fill="yellow")
snow = []
r = 5

for i in range(600):
    x = randint(0,1200)
    y = randint(0,800)
    new_snow = cvs.create_oval(x-r, y-r, x+r, y+r, outline = "white", fill = "white")
    snow.append(new_snow)

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def move_snow():
    for i in range(len(snow)):
        x,y = get_pos(snow[i])
        if y > 800:
            cvs.move(snow[i],0,-800)
        else:
            cvs.move(snow[i],0,5)

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
    
def left_click(event):
    print(event.x, event.y)
    cvs.coords(ball, event.x-25, event.y-25, event.x+25, event.y+25)

cvs.bind_all('<Key>', key_press)
cvs.bind_all('<Button-1>', left_click)

while True:
    sleep(0.005)
    try:
        window.update()
    except TclError:
        break