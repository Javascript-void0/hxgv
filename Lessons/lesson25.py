# Keyboard import, use keyboard
# "Base Video Game"

from tkinter import Tk, Canvas, TclError
from time import sleep

window=Tk()

window.title("Animation")
cvs=Canvas(window, height=800, width=1200, bg="blue")
cvs.pack()

ball_speed_x = 2
ball_speed_y = 2
ball_r = 5
ball=cvs.create_oval(50-ball_r, 50-ball_r, 50+ball_r, 50+ball_r, outline="red", fill="yellow")
brick_width = 56
brick_height = 10
brick_gap = 4

brick = []
for i in range(0, 15):
    for j in range(0, 25):
        x = 100 + i * (brick_width + brick_gap)
        y = 50 + j * (brick_height + brick_gap)
        brick_id = cvs.create_rectangle(x-brick_width//2, y-brick_height//2, 
                                        x+brick_width//2, y+brick_height//2, 
                                        outline="yellow", fill="red")
        brick.append(brick_id)
    
def get_pos(id): #id=ball
    pos=cvs.coords(id)
    x=(pos[0]+pos[2])//2
    y=(pos[1]+pos[3])//2
    return x,y

def move_ball():
    global ball_speed_x, ball_speed_y
    cvs.move(ball, ball_speed_x, ball_speed_y)
    x, y = get_pos(ball)
    if x > 1200 or x < 0:
        ball_speed_x = -ball_speed_x
    if y > 800 or y < 0:
        ball_speed_y = -ball_speed_y

def key_press(event):
    print(event.keysym)    
    if event.keysym=="Up" or event.keysym=="w":
        cvs.move(ball, 0, -5)
    if event.keysym=="Down" or event.keysym=="s":
        cvs.move(ball, 0, 5)
    if event.keysym=="Left" or event.keysym=="a":
        cvs.move(ball, -5, 0)
    if event.keysym=="Right" or event.keysym=="d":
        cvs.move(ball, 5, 0)
    
cvs.bind_all('<Key>', key_press)

while True:
    sleep(0.005)
    try:
        move_ball()
        window.update()
    except TclError:
        break