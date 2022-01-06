i = int(input())
lists = []

for j in range(i):
    lists.append(input())

duplication_test = []
results = 0
result = 0
for i in lists:
    string_list = list(i)
    for j in range(len(string_list)):
        if string_list[j] not in duplication_test:
            duplication_test.append(string_list[j])
            results += 1
        elif string_list[j - 1] != string_list[j]:
            results = 0
            break
    string_list = []
    duplication_test = []
    if results != 0:
        result += 1
    results = 0

print(result)