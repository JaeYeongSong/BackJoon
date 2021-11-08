import copy
l = int(input())
a = copy.deepcopy(l)
count = 0

while True:
    l = int(l)

    if l < 10:
        l = str(l)
        l = '0' + l

    l = str(l)
    x = int(l[0]) + int(l[1])
    x = int(x)

    if x < 10:
        x = str(x)
        x = '0' + x

    x = str(x)
    l = str(l)
    l = l[1] + x[1]
    
    count += 1
    if int(l) == int(a):
        print(count)
        break