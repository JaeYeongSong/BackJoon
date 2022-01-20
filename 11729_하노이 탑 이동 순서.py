lists = []

def move(n, x, y):
    if n > 1:
        move(n - 1, x, 6 - x - y)
    lists.append(f'{x} {y}')

    if n > 1:
        move(n - 1, 6 - x - y, y)

move(int(input()), 1, 3)
print(len(lists))

for i in lists:
    print(i)