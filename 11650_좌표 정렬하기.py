import sys

l = []
n = int(input())

for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort()
for i in l:
    sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')