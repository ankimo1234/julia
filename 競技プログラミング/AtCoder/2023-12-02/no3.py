from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

d = defaultdict(list)


for i,x in enumerate(A):
    d[x].append(i) 

d = (sorted(d.items()))
ans = [0]*N
s = 0
# for x, cnts in sorted
for i,cnts in reversed(d):
    for cnt in cnts:
        ans[cnt] = s
    s += i*len(cnts)
print(*ans)