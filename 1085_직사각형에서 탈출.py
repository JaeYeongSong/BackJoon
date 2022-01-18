x, y, w, h = map(int, input().split())

a = w - x
b = h - y

min_n = a
if min_n > b:
    min_n = b
if min_n > x:
    min_n = x
if min_n > y:
    min_n = y

print(min_n)