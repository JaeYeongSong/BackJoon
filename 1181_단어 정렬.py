import sys

n = int(input())
word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip())

set_word = list(set(word)) # 중복제거

sort_word = []
for i in set_word:
    sort_word.append((len(i), i)) # (len(word). word)로 저장

result = sorted(sort_word)

for len_word, word in result:
    sys.stdout.write(word + '\n')