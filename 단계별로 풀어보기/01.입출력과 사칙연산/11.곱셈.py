a = input()
b = input()
a_int = int(a)


def f_b(index):
    return int(b[index])


print(a_int * f_b(2))
print(a_int * f_b(1))
print(a_int * f_b(0))
print(a_int * int(b))
