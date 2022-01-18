t = int(input())

def prime(num):
    if num < 2:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True

for _ in range(t): 
    n = int(input())
    a = int(n / 2)
    b = int(n / 2)
    for k in range(int(n / 2)):
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a = a - 1
            b = b + 1