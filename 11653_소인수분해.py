n = int(input())

def find_prime(num):
    if 1 < num:
        i = 2
        while i <= num:
            if num % i == 0:
                num = num / i
                print(i)
            else:
                i += 1

find_prime(n)