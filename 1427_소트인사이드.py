import sys

n = list(sys.stdin.readline().strip())
n.sort(reverse=True)

for i in n:
    sys.stdout.write(i)