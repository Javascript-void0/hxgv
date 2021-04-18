from tkinter import Tk, Canvas, TclError
from time import sleep

window=Tk()

window.title("Painter")
cvs=Canvas(window, height=800, width=1200, bg="gray")
cvs.pack()

dot_r=5
dot=[]
eraser_sz=25
eraser=cvs.create_rectangle(-eraser_sz*2,-eraser_sz*2,0,0, outline="pink",fill="pink")

color=["red","purple","yellow","green","blue"]
active_color=0
color_txt = []
for i in range(len(color)):
    if active_color==i:
        txt=cvs.create_text(100+i*200,50,text=color[i], font = ('Helvetica', 40), fill = color[i])
    else:
        txt=cvs.create_text(100+i*200,50,text=color[i],font = ('Helvetica', 20),fill = color[i])
    color_txt.append(txt)


def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def key_press(event):
    global active_color
    print(event.keysym)
    if event.keysym>='1' and event.keysym<='5':
        cvs.itemconfig(color_txt[active_color], font = ('Helvetica', 20))
        active_color=int(event.keysym)-1
        cvs.itemconfig(color_txt[active_color], font = ('Helvetica', 40))     

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
    new_dot=cvs.create_oval(event.x-dot_r, event.y-dot_r, event.x+dot_r, event.y+dot_r, outline=color[active_color], fill=color[active_color])
    dot.append(new_dot)

def right_release(event):
    cvs.coords(eraser, -eraser_sz*2,-eraser_sz*2,0,0)

cvs.bind_all('<Key>', key_press)
cvs.bind_all('<Button-1>', left_click)
cvs.bind_all('<B1-Motion>', left_move)
cvs.bind_all('<B3-Motion>', right_move)
cvs.bind_all('<ButtonRelease-3>', right_release)

while True:
    sleep(0.005)
    try:
        window.update()
    except TclError:
        break