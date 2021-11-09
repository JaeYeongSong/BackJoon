import sys
a = []

for i in range(9):
	a += [int(sys.stdin.readline())]

for j in range(9):
    if a[j] == max(a):
        break
print(max(a))
print(j + 1)