import math
l = int(input())

for i in range(l):
    a = input().split()
    a = list(map(int, a))
    b = 0
    c = 0
    d = 0

    for j in range(1, len(a)):
        b += a[j]
    c = b / a[0]

    for x in range(1, len(a)):
        if c < a[x]:
            d += 1
    
    print(str('%.3f' % round(d / a[0] * 100, 3)) + '%')