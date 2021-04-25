# E
# C
# 
# A
# 

def move_zeros(nums):
    res = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(nums[i])
        else:
            count += 1
    for i in range(count):
        res.append(0)
    return res

sum = 0
for i in range(1, 30):
    if i * i <= 500:
        sum = sum + i * i
    else:
        break
print(sum)

def is_square_num(num):
    for i in range(1, num):
        if i * i:
            return i
    return -1