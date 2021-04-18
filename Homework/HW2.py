'''
num1=3
num2=3
for i in range(0,4,1):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
'''
'''
num1=3
num2=3
for i in range(0,4,1):
    num3=num1+num2
    print(num3)
    num2=num3
    num1=num2
'''
'''
num1=10
num2=8
for i in range(0,4,1):
    num3=num1-num2
    print(num3)
    num1=num2
    num2=num3
'''
'''
num1=1
print(num1)
num2=1
print(num2)
num3=1
print(num3)
num4=num1+num2+num3
print(num4)

sum=num1+num2+num3

for i in range(0,5,1):
    num1=num2
    num2=num3
    num3=num4
    num4=num1+num2+num3
    print(num4)
    sum=sum+num4
'''
num1=1
print(num1)
num2=1
print(num2)
num3=1
print(num3)
num4=num1+num2+num3
print(num4)

one=num1+num2+num3
sum=num1+num2+num3

for i in range(0,6,1):
    num1=num2
    num2=num3
    num3=num4
    num4=num1+num2+num3
    print(num4)
    sum=sum+num4
print(sum+one)








