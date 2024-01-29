N,L,R = map(int,input().split())
A = list(map(int,input().split()))
ans = []
for x in A:
    if x <= L:
        ans.append(str(L))
    elif L < x < R:
        ans.append(str(x))
    elif R <= x:
        ans.append(str(R))
print(' '.join(ans))