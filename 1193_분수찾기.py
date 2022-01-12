n = int(input())

line = 1
while line < n:
    n -= line
    line += 1

if line % 2 == 0: # line이 짝수번째 줄이라면
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n

print(a, '/', b, sep='')