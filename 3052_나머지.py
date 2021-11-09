import sys
a = []
b = []
count = []

for i in range(10):
    a += [int(sys.stdin.readline())]
    b += [a[i] % 42]

# 중복 check
for j in b:
    if j not in count: # 만약 count에 j가 없다면
        count.append(j) # count에 j를 추가
print(len(count))