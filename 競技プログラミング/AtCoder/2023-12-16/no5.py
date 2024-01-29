from collections import defaultdict
import sys
d = defaultdict(int)
N = int(input())
Q = [list(map(int,input().split())) for _ in range(N)]

count = 0
cnt = 0
ans = ''
for i,X in enumerate(reversed(Q)):
    t = X[0]
    x = X[1]
    if t == 2:
        d[x] += 1
        cnt += 1
        count = max(count,cnt)
    if t == 1:
        if d[x] >= 1:
            d[x] -= 1
            ans = '1 ' + ans
            cnt -= 1
        else:
            ans = '0 ' + ans

for v in d.values():
    if v > 0:
        print(-1)
        sys.exit()

print(count)
print(ans)