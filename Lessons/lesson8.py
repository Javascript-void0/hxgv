'''
num1=int(input("Please input a number: "))
num2=int(input("Please input another numer: "))

gcf=1
for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        gcf=i
print("GCF is", gcf)
'''
import turtle

t=turtle.Pen()
t.speed(0)

for i in range(300):
    if i%4==0:
        t.color("blue")
    elif i%4==1:
        t.color("red")
    elif i%4==2:
        t.color("yellow")
    else:
        t.color("green")
    t.forward(50+i)
    t.left(59)