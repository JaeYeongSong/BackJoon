import sys
from collections import Counter

n = int(sys.stdin.readline())
l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()
l_s = Counter(l).most_common()

print(round(sum(l) / n))
print(l[n // 2])

if len(l_s) > 1:
    if l_s[0][1] == l_s[1][1]:
        print(l_s[1][0])
    else:
        print(l_s[0][0])
else:
    print(l_s[0][0])

print(l[-1] - l[0])