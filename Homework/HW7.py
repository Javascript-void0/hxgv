'''
num1=1
num2=1
num3=num1+num2
print(num3)

sum=num1+num2+num3

for i in range(1,18,1):
    num1=num2
    num2=num3
    num3=num1+num2
    if num3%2==0:
         print(num3)
'''
'''
for i in range(1,101):
    if 100%i==0:
        print(i)
'''
num1=int(input("Please input a number: "))
for i in range(1,num1+1):
    if num1%i==0:
        print(i)