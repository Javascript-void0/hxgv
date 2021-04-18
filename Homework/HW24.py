# C
# B
# A
# E
# C

def square30005():
    for x in range(180):
        for y in range(180):
            if (x ** 2) + (y ** 2) == 30005:
                print(x, y)

def list_add_up(nums):
    res = [1]
    for i in range(1, len(nums)):
        res.append(nums[i-1] + nums[i])
    res.append(1)
    return res

pascal = [1]
print(pascal)
for i in range(9):
    new_p = list_add_up(pascal)
    print(new_p)
    pascal = new_p