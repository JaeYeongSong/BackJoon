import sys

l = []
n = int(input())

for i in range(n):
    x, y = sys.stdin.readline().split()
    l.append(list(map(int, [y, x])))
    
l.sort()
for i in l:
    sys.stdout.write(str(i[1]) + ' ' + str(i[0]) + '\n')