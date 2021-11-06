a = input().split()
h = int(a[0])
m = int(a[1])

if 45 <= m:
    m += -45
    print(str(h) + ' ' + str(m))
else:
    h += -1
    if h < 0:
        h += 24
    m += 60
    m += -45
    print(str(h) + ' ' + str(m))
