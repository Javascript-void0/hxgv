from tkinter import *
from time import sleep

window=Tk()

window.title("Animation")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

balls=[]
for i in range(5):
    ball=cvs.create_oval(100*i,100*i,100*i+50,100*i+50,outline="red", fill="yellow")
    balls.append(ball)
speed_x=[2,2,2,2,2] #Called in function with global
speed_y=[2,2,2,2,2]

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def detect_edge():
    global speed_x,speed_y #Variable outside Function
    for i in range(len(balls)):
        x,y=get_pos(balls[i])
        if y>=800:
            speed_y[i]=-speed_y[i]
        if x>=1200:
            speed_x[i]=-speed_x[i]
        if y<0:
            speed_y[i]=-speed_y[i]
        if x<0:
            speed_x[i]=-speed_x[i]

while True:
    sleep(0.005)
    detect_edge()
    for i in range(len(balls)):
        cvs.move(balls[i], speed_x[i], speed_y[i])
        speed_y[i]=speed_y[i]+1
    window.update()
