l = int(input())
a = input().split()
a = list(map(int, a))
b = []
c = 0

for i in a:
    b += [i / max(a) * 100]

for j in b:
    c += j

print(c / l)