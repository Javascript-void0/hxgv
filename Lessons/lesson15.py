from tkinter import *
from time import sleep

window=Tk()

window.title("Animation")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball=cvs.create_oval(50,50,100,100,outline="red", fill="yellow")

while True:
    sleep(0.01)
    cvs.move(ball, 2, 2)
    window.update()

# w.mainloop()
