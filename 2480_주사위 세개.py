a, b, c = list(map(int, input().split()))

sum = 0
if a == b and b == c and a == c:
    sum += 10000 + a * 1000
elif a == b:
    sum += 1000 + a * 100
elif b == c:
    sum += 1000 + b * 100
elif a == c:
    sum += 1000 + c * 100
else:
    sum += max(a, b, c) * 100
print(sum)