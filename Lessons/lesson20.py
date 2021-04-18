from tkinter import Tk, Canvas, TclError
from time import sleep

window=Tk()

window.title("Painter")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

dot_r=5
dot=[]
eraser_sz=25
eraser=cvs.create_rectangle(-eraser_sz*2,-eraser_sz*2,0,0, outline="pink",fill="pink")

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def key_press(event):
    print(event.keysym)    

def left_click(event):
    print(event.x, event.y)

def erase_dot(x,y):
    for i in range(len(dot)-1,-1,-1):
        dx, dy=get_pos(dot[i])
        if (dx>=x-eraser_sz and dx<=x+eraser_sz and dy>=y-eraser_sz and dy<=y+eraser_sz):
            cvs.delete(dot[i])
            del dot[i]

def right_move(event):
    cvs.coords(eraser, event.x-eraser_sz, event.y-eraser_sz, event.x+eraser_sz, event.y+eraser_sz)
    erase_dot(event.x, event.y)

def left_move(event):
    new_dot=cvs.create_oval(event.x-dot_r, event.y-dot_r, event.x+dot_r, event.y+dot_r, outline="red", fill="red")
    dot.append(new_dot)

cvs.bind_all('<Key>', key_press)
cvs.bind_all('<Button-1>', left_click)
cvs.bind_all('<B1-Motion>', left_move)
cvs.bind_all('<B3-Motion>', right_move)

while True:
    sleep(0.005)
    try:
        window.update()
    except TclError:
        break