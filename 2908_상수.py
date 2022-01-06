string = input().split()
lists = []

for i in range(len(string)):
    lists.append(string[i][::-1])

lists = list(map(int, lists))

maximum = lists[0]
if maximum < lists[1]:
    maximum = lists[1]

print(maximum)