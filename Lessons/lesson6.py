import turtle

t=turtle.Pen()
t.speed(0)
t.color('blue')

for i in range(6):
    t.circle(50)
    t.up()
    t.forward(80)
    t.left(60)
    t.down()
