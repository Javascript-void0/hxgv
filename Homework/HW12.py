'''
nums=[4,3,5,6,3,4,7,9]
nums1=[]
nums2=[]
for i in range(0,len(nums)):
    if nums[i]%2==0: 
        nums1.insert(0,nums[i])
    else:
        nums2.insert(0,nums[i])
print(nums1)
print(nums2)
'''
'''
nums1=[1,2,3,4,5]
nums2=[6,7,8,9,10]
nums=[]
for i in range (len(nums1)):
    nums.append(nums2[4-i])
    nums.append(nums1[i])
print(nums)
'''
'''
list=[1,1]
num1=1
num2=1
num3=num1+num2
print(num3)

for i in range(1,8,1):
    num1=num2
    num2=num3
    num3=num1+num2
    print(num3)
    list.append(num3)
print(list)
'''
list=[]
for num in range(2,101):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime==True:
        list.append(num)
print(list)