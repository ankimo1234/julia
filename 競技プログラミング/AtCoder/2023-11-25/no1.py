N, L = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for x in A:
    if x >= L:
        cnt += 1
print(cnt)
