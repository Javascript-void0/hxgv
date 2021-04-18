nums=[3,5,0,0,4,0,0,0,0]
for i in range(len(nums)-1,-1,-1):
    if nums[i]==0:
        del nums[i]
print(nums)

# Start backwards, else delete will effect index number. 