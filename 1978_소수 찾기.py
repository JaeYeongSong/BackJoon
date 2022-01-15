t = int(input())
n = list(map(int, input().split()))

def is_prime_number(list):
    sum = 0
    for i in list:
        err = 0
        if 1 < i:
            for j in range(2, i):
                if i % j == 0:
                    err += 1
            if err == 0:
                sum += 1
    return sum

print(is_prime_number(n))