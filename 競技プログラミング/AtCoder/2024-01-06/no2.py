
N = int(input())
N += 1
for i in range(N):
    for j in range(N-i):
        for k in range(N-i-j):
            print(i,j,k)