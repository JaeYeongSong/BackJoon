n = int(input())

for i in range(1, n + 1):
    num = sum((map(int, str(i)))) # i의 각 자릿수를 더함
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)