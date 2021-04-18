from math import sqrt

def find_idx(nums,num):
    for i in range(len(nums)):
        if nums[i]==num:
            return i
    return -1

def remove_dup(nums):
    res=[]
    for i in range(len(nums)):
        if find_idx(res,nums[i]) == -1:
            res.append(nums[i])
    return res

nums=[1,6,3,4,3,2,5,4,1,2]
print(remove_dup(nums))

def get_distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

print(get_distance(0,0,3,4))

def inside_circle(center_x, center_y, radius, x, y):
    dist = get_distance(center_x, center_y, x, y)
    if dist < radius:
        return 1
    elif dist == radius:
        return 0
    else:
        return -1

print(inside_circle(3,3,5,4,4))
print(inside_circle(3,3,5,7,6))
print(inside_circle(3,3,5,8,8))