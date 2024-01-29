N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A_max = 10**6
B_max = 10**6
for q,a,b in zip(Q,A,B):
    if a != 0:
        A_max = min(A_max,q//a)
    if b != 0:
        B_max = min(B_max,q//b)

cnt = 0
if A_max >= B_max:
    while B_max+1:
        A_cnt = A_max
        for q,a,b in zip(Q,A,B):
            if a != 0:
                A_cnt = min(A_cnt,(q-b*B_max)//a)
        cnt = max(cnt,A_cnt+B_max)
        B_max -= 1

else:
    while A_max+1:
        B_cnt = B_max
        for q,a,b in zip(Q,A,B):
            if b != 0:
                B_cnt = min(B_cnt,(q-a*A_max)//b)
        cnt = max(cnt,B_cnt+A_max)
        A_max -= 1
print(cnt)