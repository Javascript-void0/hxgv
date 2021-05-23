fin = open ('./Lessons/lesson29.in', 'r')
line = fin.readline().strip().split()
b_b = int(line[0])
b_a = int(line[1])

line = fin.readline().strip().split()
s_b = int(line[0])
s_a = int(line[1])

line = fin.readline().strip().split()
g_b = int(line[0])
g_a = int(line[1])

line = fin.readline().strip().split()
p_b = int(line[0])
p_a = int(line[1])

gtp = p_a - p_b
stg = g_a - g_b + gtp
bts = s_a - s_b + stg

print(bts, stg, gtp)

fout = open('./Lessons/lesson29.out', 'w')
fout.write(str(bts))
fout.write('\n')
fout.write(str(stg))
fout.write('\n')
fout.write(str(gtp))
fout.close()