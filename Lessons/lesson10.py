'''
num=9
print (num,"=",end='  ')
for i in range(2,num+1): 
    while num%i==0:
        num=num//i
        if num==1:
            print(i,end=' ')
        else:
            print(i,"x",end=' ')
'''
num=323543
count=0
while num>0:
    digit=num%10
    num=num//10
    print(digit)
    if digit==3:
        count=count+1
print("There are",count, "digit 3.")