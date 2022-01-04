i = int(input())

for j in range(i):
    a = input().split()
    result = ''
    for x in a[1]:
        result += x * int(a[0])
    print(result)