# 2 ~ 7 (6)
# 8 ~ 19 (12)
# 20 ~ 37 (18)
# 38 ~ 61 (24)
# 6의 배수

number = int(input())
honeycomb = 1

i = 1
while honeycomb < number:
    honeycomb += 6 * i
    i += 1
print(i)