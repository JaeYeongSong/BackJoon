l = int(input())
for i in range(l):
    b = input().split()
    c = int(b[0])
    d = int(b[1])
    print('Case #' + str(i + 1) + ': ' + str(c) + ' + ' + str(d) + ' = ' + str(c + d))
