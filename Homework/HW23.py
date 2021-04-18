# B
# C
# B / E
# A
# E / C

def get_longest_str(list_str):
    longest = list_str[0]
    for i in range(len(list_str)):
        x = list_str[i]
        if len(x) > len(longest):
            longest = list_str[i]
    return longest

# print(get_longest_str(["123", "abcd", "ABC", "1a2b"]))

def merge_str(list_str):
    new = ""
    for i in range(len(list_str)):
        new = new + list_str[i]
    return new

# print(merge_str(["123", "abcd", "ABC", "1a2b3c"]))

def str_has_num(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 48) and (ord(str[i]) <= 57):
            return True
    return False

# print(str_has_num("abcd"))
# print(str_has_num("1234"))
# print(str_has_num("1a2b"))