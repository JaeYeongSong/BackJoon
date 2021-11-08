a = int(input())

for i in range(a):
    i += 1
    b = a - i
    print(' ' * b, end='')
    print('*' * i)