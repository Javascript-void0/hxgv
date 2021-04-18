'''
num1=int(input("Please input a number: "))
num2=int(input("Please input another: "))

lcm=num1
for i in range(num1,num1*num2+1):
    if i%num1==0 and i %num2==0:
        lcm=i
        break
print("LCM is",lcm)
'''
for i in range(1,101):
    if i%9==0 and i%7 != 0:
        print(i)