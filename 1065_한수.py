def hansu(num):
    result = 0
    for i in range(1, num+1):
        listI = list(map(int, str(i)))
        if i < 100:
            result += 1
        elif listI[0] - listI[1] == listI[1] - listI[2]:
            result += 1
    return result

num = int(input())
print(hansu(num))