while True:
    x, y, z = list(map(int, input().split()))
    if x == 0 and y == 0 and z == 0:
        break
    max_list = [x, y, z]
    c = max(max_list)
    del max_list[max_list.index(c)]
    a = max_list[0]
    b = max_list[1]
    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")