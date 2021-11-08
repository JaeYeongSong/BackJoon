while True:
    try:
        a = input().split()
        a = list(map(int, a))
        print(a[0] + a[1])
    except EOFError: # 오류처리 해 주어야 함
        break