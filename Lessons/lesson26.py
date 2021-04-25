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

bar_width = 200
bar_height = 6
bar = cvs.create_rectangle(0, 600-bar_height, bar_width, 600, outline="green", fill="pink")

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

def det_ball_brick_collission():
    global ball_speed_y
    x, y = get_pos(ball)
    for i in range(len(brick)):
        pos_brick = cvs.coords(brick[i])
        if (x > pos_brick[0] and
            x < pos_brick[2] and
            y > pos_brick[1] and 
            y < pos_brick[3]):
            cvs.delete(brick[i])
            del brick[i]
            ball_speed_y = -ball_speed_y
            return

def det_ball_bar_collision():
    global ball_speed_y
    x, y = get_pos(ball)
    pos_bar = cvs.coords(bar)
    if (x > pos_bar[0] and
        x < pos_bar[2] and
        y > pos_bar[1] and 
        y < pos_bar[3]):
        ball_speed_y = -ball_speed_y
        return

def key_press(event):
    print(event.keysym)    
    if event.keysym=="Left" or event.keysym=="a":
        cvs.move(bar, -20, 0)
    if event.keysym=="Right" or event.keysym=="d":
        cvs.move(bar, 20, 0)
    
cvs.bind_all('<Key>', key_press)

while True:
    sleep(0.005)
    try:
        move_ball()
        det_ball_brick_collission()
        det_ball_bar_collision()
        window.update()
    except TclError:
        break