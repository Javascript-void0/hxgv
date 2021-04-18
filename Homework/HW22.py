# B
# nums2=nums1 >>> Refers to the same list
# nums2=nums1.copy() COPY to new list
# C
# A
# D
# B

def get_turn_degree(dir1, dir2):
    if dir1 == 'E':
        if dir2 == 'N':
            return -90
        if dir2 == 'S':
            return 90
    if dir1 == 'S':
        if dir2 == 'E':
            return -90
        if dir2 == 'W':
            return 90
    if dir1 == 'W':
        if dir2 == 'S':
            return -90
        if dir2 == 'N':
            return 90
    if dir1 == 'N':
        if dir2 == 'W':
            return -90
        if dir2 == 'E':
            return 90
    return 0

print(get_turn_degree('N', 'E'))
print(get_turn_degree('E', 'N'))

def get_total_turn(str1):
    ans = 0
    for i in range(len(str1)-1):
        ans = ans + get_turn_degree(str1[i], str1[i+1])
    return ans

print(get_total_turn("NESW"))
print(get_total_turn("WSSSEENWNEESSENNNNWWWS"))
