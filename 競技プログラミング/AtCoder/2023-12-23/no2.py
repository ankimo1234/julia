
A, M, L, R = map(int,input().split())

if R == L:
    ans = 0
elif A <= L:
    start = (int((L-A-1)/M))
    end = (int((R-1-A)/M))
    ans = end - start

elif L < A < R:
    left = int((A-L+1)/M-1)
    right = int((R-L-1)/M-1)
    ans = left + right + 1

elif R <= A:
    start = int((A-R+1)/M)
    end = int((A-L+1)/M)
    ans = end - start
print(ans)