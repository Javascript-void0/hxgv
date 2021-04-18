# Keyboard import, use keyboard
# "Base Video Game"

from tkinter import Tk, Canvas, TclError
from time import sleep

window=Tk()

window.title("Animation")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball=cvs.create_oval(50,50,100,100,outline="red", fill="yellow")

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

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