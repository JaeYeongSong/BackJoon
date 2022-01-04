string  = input()

a_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # a-z
result = ''

for i in a_z:
    result += str(string.find(i)) # index, -1
    result += ' ' # 공백

print(result)