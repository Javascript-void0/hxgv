''' 
# in Shell
num=[1,2,3]
num
num[0]
len(num)
num[0]=3
'''
'''
nums=[2,4,6,3,5,7,1,4]
count=0
for i in range(0,len(nums)):
    if nums[i]%2==0:
        count=count+1
print("There are",count,"even numbers")
'''
'''
nums=[9,5,-2,-3,5,4,-4,-6]
for i in range(0,len(nums)):
    if nums[i]<0:
        nums[i]=0
print(nums)
'''
nums=[-3,-4,-2,-6,-4,-3,-7,-4,-3]
res=nums[0]
for i in range(0,len(nums)):
    if nums[i]>res:
        res=nums[i]
print("Max value is",res)