def teleport(a,b,x,y):
    d1 = abs(a-b)
    d2 = abs(a-x)+abs(b-y)
    d3 = abs(a-y)+abs(b-x)
    print(d1,d2,d3)
    if d1 <= d2 and d1 <= d3:
        return d1
    elif d2 <= d1 and d2 <= d3:
        return d2
    else:
        return d3

print(teleport(3,10,8,2))

print(teleport(86,84,15,78))

print(teleport(35,94,92,87))