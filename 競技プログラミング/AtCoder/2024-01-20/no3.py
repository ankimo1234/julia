from collections import defaultdict
d = defaultdict(int)
N = int(input())
A = list(map(int,input().split()))
for i,a in enumerate(A):
    d[a] = i+1

x = d[-1]
ans = [str(x)]
for _ in range(N-1):
    x = d[x]
    ans.append(str(x))
print(" ".join(ans))