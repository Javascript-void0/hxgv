'''
num1=345
num2=345

if num1 > num2:
    print("num1 is bigger than num2")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num1 is smaller than num2")
'''
'''
num=int(input("Please input a number: "))
if num%2==1:
    print(num, "is odd")
else:
    print(num, "is even")
'''
num1=int(input("Please input a number: "))
num2=int(input("Please input a dividor: "))
if num1%num2==0:
    print(num1, "can be fully divided by", num2)
else:
    print(num1, "can not be fully divided by", num2)