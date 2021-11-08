a = input().split()
b = input().split()
a = list(map(int, a))
b = list(map(int, b))
c = ''

for i in range(a[0]):
    if b[i] < a[1]:
        c += str(b[i]) + ' '
print(c)