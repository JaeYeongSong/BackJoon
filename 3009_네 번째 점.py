a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

lists = []
listss = []
for i in [a, b, c]:
    lists.append(i[0])

if lists.count(lists[0]) == 2:
    i = lists[0]
    lists.remove(i)
    lists.remove(i)
elif lists.count(lists[1]) == 2:
    i = lists[1]
    lists.remove(i)
    lists.remove(i)

for i in [a, b, c]:
    listss.append(i[1])

if listss.count(listss[0]) == 2:
    i = listss[0]
    listss.remove(i)
    listss.remove(i)
elif listss.count(listss[1]) == 2:
    i = listss[1]
    listss.remove(i)
    listss.remove(i)

print(lists[0], listss[0])