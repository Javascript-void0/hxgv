from tkinter import Tk, Canvas, TclError
from time import sleep

window=Tk()

window.title("Rings")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ring = []

def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x, y
    
def left_click(event):
    print(event.x, event.y)
    new_ring = cvs.create_oval(event.x-2, event.y-2, event.x+2, event.y-2, outline="yellow")
    ring.append(new_ring)

def update_ring():
    for i in range(len(ring)):
        pos = cvs.coords(ring[i])
        cvs.coords(ring[i], pos[0]-2, pos[1]-2, pos[2]+2, pos[3]+2)

cvs.bind_all('<Button-1>', left_click)

while True:
    sleep(0.005)
    try:
        window.update()
        update_ring()
    except TclError:
        break

    