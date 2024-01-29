N = int(input())
A = list(map(int,input().split()))
A.sort()
A.reverse()
num = max(A)
for i in range(N):
    if A[i] != num:
        print(A[i])
        break
