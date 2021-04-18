def reverse_digit(num):
    rev = 0
    while num>0: 
        a = num % 10
        rev = rev * 10 + a 
        num = num // 10
    return rev

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def is_even(num):
    if num%2==0:
        return True
    return False

def check_goldbach(num):
    for i in range(2,num):
        if (is_prime(i)==True) and (is_prime(num-i)==True):
            return i,num-i
for num in range(100,200,2):
    print(num,"is sum of", check_goldbach(num))