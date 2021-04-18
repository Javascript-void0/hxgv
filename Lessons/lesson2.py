num1=123
num1=234

# num1 is overwritten by 234

num2=345
sum=num1+num2
print(sum)

# = is to set value
# == is check is value is same (True/False)

sum=1+2+3+4+5+6+7+8+9+10
print(sum)

for i in range(0,101,10):
    print(i)
    
# need three numbers
# "i" is a loop variable
# first number is initial value
# second number is end/final number
# third number is step

for i in range(0,101,10):
    print(i)
print("Hello")
print("world")


# with tab us inside for loop
# without tab is outside for loop

# cannot continue for loop after end
# Ex. for i in range(0,101,10):
#     print(i)
# print("Hello")
#     print("world")<- Error

for i in range(10,0,-1):
    print(i)

# reverse loop


# Keep adding to variable (in Shell)
# >>> sum=0
# >>> sum=sum+1
# >>> sum
# 1
# >>> sum=sum+2
# >>> sum
# 3
# >>> sum=sum+3
# >>> sum
# 6

sum=0
for i in range(1,101,1):
    sum=sum+i
    
print(sum)
# =5050

# String (in Shell)
# >>> char1='a'
# >>> char1+'a'
# 'aa'

sign='a'
char1=sign
for i in range(0,10,1):
    print(char1)
    char1=char1+sign
# a
# aa
# aaa
# aaaa
# aaaaa
# aaaaaa
# aaaaaaa
# aaaaaaaa
# aaaaaaaaa
# aaaaaaaaaa
# change the value of sign='...' to change char. 

