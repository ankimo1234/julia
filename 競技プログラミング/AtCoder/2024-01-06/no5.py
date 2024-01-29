from collections import defaultdict
N, M = map(int,input().split())
A = list(map(int,input().split()))
M = [list(map(int,input().split())) for _ in range(M)]
d = defaultdict(list)


for m in M:
    if A[m[0]-1] < A[m[1]-1]:
        d[m[0]] += [m[1]]
    else:
        d[m[1]] += [m[0]]
print(d)
cnt = 0
if 1 in d:
    x = d[1]
    while x:
        cnt += 1
        xxx = []
        for xx in x:
            for dd in d[xx]:
                xxx.append(dd)
        x = xxx
print(cnt)