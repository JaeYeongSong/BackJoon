import sys

n = int(input())
user = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    user.append([int(age), i, name])

result = sorted(user)

for age, data, name in result:
    sys.stdout.write(str(age) + ' ' + name + '\n')