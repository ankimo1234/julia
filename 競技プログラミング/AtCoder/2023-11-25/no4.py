N = int(input())
box = [input() for _ in range(N)]
width_cnt = []
height_cnt = []


for i in range(N):
    cnt = 0
    width_cnt.append(box[i].count('o'))
    for j in range(N):
        if box[j][i] == 'o':
            cnt += 1
    height_cnt.append(cnt)


ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if box[i][j] == 'o':
            if width_cnt[i] >= 2 and height_cnt[j] >= 2:
                ans += (width_cnt[i]-1)*(height_cnt[j]-1)

print(ans)
