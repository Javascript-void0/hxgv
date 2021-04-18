def find_idx(nums,num):
    idx=0
    for i in range(len(nums)):
        if nums[i]==num:
            idx=i
            return i
    return -1
print(find_idx([1,2,3,4,5],3))

def get_common(nums1,nums2):
    res=[]
    for i in range(len(nums1)):
        if find_idx(nums2, nums1[i])>-1:
            res.append(nums1[i])
    return res
print(get_common([1,2,3,5,6],[2,4,6,7,8]))

def remove_common(nums1,nums2):
    res=[]
    for i in range(len(nums1)):
        if find_idx(nums2,nums1[i])==-1:
            res.append(nums1[i])
    return res
print(remove_common([1,2,3,5,6],[2,4,6,7,8]))