N = int(input().split()[0])
box = []
for i in range(N):
    box.append(input().split())
cnt = []
for i in range(24):
    cnt_num = 0
    for j in range(N):
        if 0 <= i - int(box[j][1]) <= 8:
            cnt_num += int(box[j][0])
        elif int(i) >= 16:
            if 0 <= i - int(box[j][1])  <= 8:
                cnt_num += int(box[j][0])
        elif int(i) <= 7:
            if 0 <= -i + int(box[j][1]) - 16 <= 8:
                cnt_num += int(box[j][0])
    cnt.append(cnt_num)
print(max(cnt))