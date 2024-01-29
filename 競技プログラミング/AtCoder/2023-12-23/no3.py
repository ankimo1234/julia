import sys
input = sys.stdin.readline


N, K = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
if int((K+1)/2) == int(K/2):
    for i in range(int(K/2)):
        ans += (A[2*i+1]-A[2*i])

elif K == 1:
    ans = 0

else:
    Gbox,Kbox = [0]*int(len(A)/2),[0]*int(len(A)/2)
    for i in range(int(int(K/2))):
        Gbox[i] = (A[2*i+1]-A[2*i])
        Kbox[i] = (A[2*i+2]-A[2*i+1])
        if i != 0:
            Gbox[i] += Gbox[i-1]
            Kbox[i] += Kbox[i-1]

    for i in range(int(len(A)/2+1)):
        if i == 0:
            ans = Kbox[-1]
        else:
            ans = min(ans, Gbox[i-1] + Kbox[-1] - Kbox[i-1])


print(ans)

