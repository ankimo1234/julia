N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
max_cnt = 1
n = 1
for i in range(N):
    if i + n >= N:
        pass
    else:
        while A[i] + M > A[i+n]:
            n += 1
            if i+n >= N:
                break
        max_cnt = max(max_cnt,n)
print(max_cnt)  