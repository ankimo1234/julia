N, Q = map(int,input().split())
P = [input() for _ in range(N)]

Pbox = []
for i in range(N):
    cnt = 0
    line = []
    for j in range(N):
        if P[i][j] == 'B':
            cnt += 1
        line.append(cnt)
    Pbox.append(line)
print(Pbox)

for _ in range(Q):
    query = list(map(int,input().split()))
    grid_height = query[2] - query[0] + 1
    grid_width = query[3] - query[1] + 1

    print(query)
    if grid_height < N:
        xbox = []
        for _ in range(N):
            x = Pbox[query[0] % N][query[3] % N] - Pbox[query[0] % N][query[1] % N] + Pbox[query[0]][-1]*(int(N/grid_width))
            x.append(xbox)
            print(10)

    else:
        x = 0
        ans = 0
        for i in range(grid_height):
            
            x = Pbox[(query[0] + i) % N][query[3] % N] - Pbox[(query[0] + i) % N][query[1] % N + 1] + Pbox[(query[0] + i) % N][-1]*(int(N/grid_width + 1))
            print(x)
            ans += x
        print(ans)

