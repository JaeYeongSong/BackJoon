import sys
a = []
b = []
count = []

for i in range(10):
    a += [int(sys.stdin.readline())]
    b += [a[i] % 42]

# 중복 check
for j in b:
    if j not in count:
        count.append(j)
print(len(count))