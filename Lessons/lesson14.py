def my_sum(num1, num2):
    ans=num1+num2
    return ans
'''
res=my_sum(1,2)
print(res)
'''
def sum_list(nums1, nums2):
    ans=[]
    for i in range(len(nums1)):
        ans.append(nums1[i]+nums2[i])
    return ans

nums1=[3,4,5,6]
nums2=[1,1,1,2]
print(sum_list(nums1,nums2))

def is_prime(nums):
    for i in range(2,nums):
        if nums%i==0:
            return False
    return True

for i in range(2,100):
    if is_prime(i)==True:
        print(i,"is prime")