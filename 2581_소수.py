min_n = int(input())
max_n = int(input())

def make_prime_number(min_n, max_n):
    sum = []
    for i in range(min_n, max_n + 1):
        err = 0
        if 1 < i:
            for j in range(2, i):
                if i % j == 0:
                    err += 1
            if err == 0:
                sum.append(i)
    return sum

def sum_number(list):
    sum = 0
    if list:
        for i in list:
            sum += i
        return sum
    else:
        return False

result = make_prime_number(min_n, max_n)

if not sum_number(result):
    print(-1)
else:
    print(sum_number(result))
    print(min(result))