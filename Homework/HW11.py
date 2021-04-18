'''
nums=[4,3,5,6,3,4,7,9]
res=nums[0]
for i in range(0,len(nums)):
    if nums[i]<res:
        res=nums[i]
print(res)
'''
'''
nums=[4,3,-5,-4,0,5,-7,8,-9]
neg=0
for i in range(0,len(nums)):
    if nums[i]<0:
        neg=neg+1
print(neg)
'''
'''
nums=[4,3,5,6,3,4,7,9]
count=0

for i in range(0,len(nums)):
    is_prime=True
    for j in range(2,nums[i]):
        if nums[i]%j==0:
            is_prime=False
            break
    if is_prime==True:
        count=count+1
print(count)
'''
nums=[12,36,48,24,12,18]
for factor in range(1,nums[0]+1):
    is_cf=True
    for i in range(0,len(nums)):
        if nums[i]%factor !=0:
            is_cf=False
    if is_cf==True:
        print(factor)