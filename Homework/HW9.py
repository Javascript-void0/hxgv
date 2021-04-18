'''
for num in range(100,201):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(num,"is prime")
'''
'''
count=0
for num in range(150,200):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime==True:
        count=count+1
print(count)
'''
count=0
for num in range(101,151):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            count=count+1
            break
print(count)