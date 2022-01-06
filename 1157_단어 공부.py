s = input().upper()
cnt = [0] * 26
for c in s:
    cnt[ord(c)-ord('A')] += 1
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    idx = cnt.index(max(cnt))
    print(chr(idx+ord('A')))