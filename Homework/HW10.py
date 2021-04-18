
count=0
num=336
for i in range(2,num+1): 
    while num%i==0:
        num=num//i
        if i == 2:
            count=count+1
print(count)

'''
num=32546845
count=0
while num>0:
    digit=num%10
    num=num//10
    if digit%2==0:
        count=count+1
print(count)
'''
'''
count=0
for i in range(1,101):
    while i%5==0:
        count=count+1
        break
print(count)
'''
'''
sum=0
for i in range(1,101):
    while i>0:
        digit=i%10
        i=i//10
        sum=sum+digit
print(sum)
'''