import sys

# counting sort에서 빈도 저장하기 위한 배열
l = [0 for _ in range(10001)]

t = int(sys.stdin.readline())

# 인풋으로 받은 수가 몇변 들어왔는지 빈도(Int) 저장
for _ in range(t):
    num = int(sys.stdin.readline())
    l[num] += 1

# 배열의 시작부터 돌며 저장된 빈도만큼 인덱스값을 출력
for i in range(1, 10001):
    count = l[i] # l의 i번 째 정수를 count에 저장
    for _ in range(count): # count 담긴 정수 만큼 반복
        sys.stdout.write(str(i) + '\n')