
N,M = map(int,input().split())
A = sorted((list(map(int,input().split()))))
print(A)
current = 0
ans = []
while True:
    i = current
    Flag = True
    cnt = 0
    while Flag:
        cnt += 1
        i += 1
        if i >= N:
            ans.append(cnt)
            Flag = False
            print(1)
        elif A[i] >= A[current] + M:
            ans.append(cnt)
            Flag = False
    if current + M -1 >= A[-1]:
        break
    current += 1
print(ans)

