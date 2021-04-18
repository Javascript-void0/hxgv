for i in range(1,10):
    for j in range(1,10-i):
        print(' ',sep='', end='')
    for j in range(1,2*i):
        print (i,sep='', end='')
#        print(i, "x", j, "=", i*j, sep='', end=' ')
    print()
