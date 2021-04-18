# Fibonacci Numbers

num1=1
num2=1
num3=num1+num2
print(num3)

sum=num1+num2+num3

for i in range(1,18,1):
    num1=num2
    num2=num3
    num3=num1+num2
    print(num3)
    sum=sum+num3
print("Sum of 20 Fibonacci Numbers is",sum)
