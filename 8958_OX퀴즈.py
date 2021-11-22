l = int(input())
b = 0
c = 0

for i in range(l):
    a = list(input())
    for j in range(len(a)):
        if a[j] == 'O':
            c += 1 + b
            b += 1
        elif a[j] == 'X':
            b = 0
    print(c)
    b = 0
    c = 0