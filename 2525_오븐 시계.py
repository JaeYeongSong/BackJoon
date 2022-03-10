h, m = list(map(int, input().split()))
c = int(input())

if c < 60:
    m += c
else:
    h += c // 60
    c -= 60 * (c // 60)
    m += c

if m >= 60:
    h += m // 60
    m -= 60 * (m // 60)

if h >= 24:
    h -= 24
print(h, m, sep=' ')