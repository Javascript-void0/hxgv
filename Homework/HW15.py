'''
def remove_zeros(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==0:
            del nums[i]
    return nums
nums=[0,4,2,0,2,4,0]
print(remove_zeros(nums))
'''
'''
def reverse_list(nums):
    reverse=[]
    for i in range(len(nums)):
        reverse.insert(nums[i])
    return reverse
nums=[1,2,3,4,5]
print(reverse_list(nums))
'''
'''
def merge_list(nums1,nums2):
    nums=[]
    for i in range(len(nums1)):
        nums.append(nums1[i])
    for i in range(len(nums2)):
        nums.append(nums2[i])
    return nums
print(merge_list([1,2,3,4,5],[6,7,8,9,10]))
'''
'''
nums=[4,3,6,2,4]
for i in range(1,len(nums),1):
    if (nums[i]>nums[i-1]):
        temp=nums[i]
        nums[i]=nums[i-1]
        nums[i-1]=temp
print(nums)
'''
