'''
nums=[4,3,5,6,3,4,7,9]
for i in range(len(nums)-1,-1,-1):
    if nums[i]%2==0: 
        del nums[i]
print(nums)
'''
'''
nums=[4,3,5,6,3,4,7,9,6,4,2]
max=nums[0]
for i in range (0,len(nums)):
    if nums[i]>max:
        max=nums[i]
print(max)
'''
'''
nums=[4,3,5,6,3,4,7,9,6,4,2]
max=nums[0]
for i in range (0,len(nums)):
    if nums[i]>max:
        max=nums[i]
for i in range (0,len(nums)-1):
    if nums[i]==max:
        del nums[i]
print(nums)
'''
'''
nums=[4,3,5,6,3,4,7,9,6,4,2]
sorted_nums=[]
max=nums[0]

for i in range (len(nums)-1,-1,-1):
    if nums[i]>=max:
        max=nums[i]
    while nums[i]==max:
        del nums[i]
        sorted_nums.append(max)
print(sorted_nums)
print(nums)
'''

nums=[4,3,5,6,3,4,7,9,6,4,2]
sorted_nums=[]

for j in range(len(nums)):
    max_value=nums[0]
    max_idx=0
    for i in range (0,len(nums)):
        if nums[i]>max_value:
            max_value=nums[i]
            max_idx=i
    print(max_idx)
    del nums[max_idx]
    print(nums)
    sorted_nums.insert(0,max_value)
print(sorted_nums)
