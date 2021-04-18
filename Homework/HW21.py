# C
# C
# A
# A
# E

def sort_nums(nums):
    res = []
    for i in range(0, len(nums)):
        idx = 0
        min = nums[0]
        for j in range(1, len(nums)):
            if min > nums[j]:
                idx = j
                min = nums[j]
        res.append(min)
        del nums[idx]
    return res

print(sort_nums([2,2,11,4,9,7,9]))

def abc(str1):
    list_str = str1.split()
    nums = []
    for i in range(len(list_str)):
        nums.append(int(list_str[i]))
    res = sort_nums(nums)
    a = res[0]
    b = res[1]
    c = res[6]-a-b
    print(a,b,c)

# abc("2 2 11 4 9 7 9")

abc(input())