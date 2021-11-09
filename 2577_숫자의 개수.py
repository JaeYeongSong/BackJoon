import sys
a = []

for i in range(3):
	a += [int(sys.stdin.readline())]

a = str(a[0] * a[1] * a[2])

for i in range(10):
    print(a.count(str(i)))