fin = open('./Lessons/lesson28.in', 'r')
line = fin.readline().split()
print(line)

def teleport(a, b, x, y):
    dab = abs(b-a)
    daxyb = abs(x-a) + abs(b-y)
    dayxb = abs(y-a) + abs(b-x)
    ans = dab
    if daxyb < ans:
        ans = daxyb
    if dayxb < ans:
        ans = dayxb
    return ans

a = int(line[0])
b = int(line[1])
x = int(line[2])
y = int(line[3])

res = teleport(a, b, x, y)
fout = open('./Lessons/lesson28.out', 'w')
fout.write(str(res))
fout.close()
fin.close()