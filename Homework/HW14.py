
def is_even(num):
    if num%2==0:
        return True
    return False

def get_lcm(num1,num2):
    for i in range(num1,num1*num2+1):
        if i%num1==0 and i%num2==0:
            return i

def count_num_even(nums):
    count=0
    for i in range(len(nums)):
        if is_even(nums[i]==True):
            count=count+1
    return count

def get_sum(nums):
    sum=0
    for i in range(len(nums)):
        sum=sum+nums[i]
    print(sum)