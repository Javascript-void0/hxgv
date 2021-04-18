from tkinter import *
from time import sleep

window=Tk()

window.title("Animation")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball=cvs.create_oval(50,50,100,100,outline="red", fill="yellow")
speed_x=2 #Called in function with global
speed_y=2

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def detect_edge():
    global speed_x,speed_y #Variable outside Function
    x,y=get_pos(ball)
    if y>=800:
        speed_y=-2
    if x>=1200:
        speed_x=-2
    if y<0:
        speed_y=2
    if x<0:
        speed_x=2

while True:
    sleep(0.0005)
    detect_edge()
    cvs.move(ball, speed_x, speed_y)
    window.update()