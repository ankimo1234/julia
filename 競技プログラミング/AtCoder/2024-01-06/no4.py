N = int(input())

box = [[[] for _ in range(N)] for i in range(N)]
cnt = N
num = 1
i,j = 0,0
while cnt > 1:
    if cnt == N:
        for l in range(cnt):
            box[i][j] = str(num)
            num += 1
            j += 1
        j -= 1
    elif cnt % 2 == 0:
        for l in range(cnt):
            i += 1
            box[i][j] = str(num)
            num += 1
        for l in range(cnt):
            j -= 1
            box[i][j] = str(num)
            num += 1
            

    elif cnt % 2 == 1:
        for l in range(cnt):
            i -= 1
            box[i][j] = str(num)
            num += 1
            
        for l in range(cnt):
            j += 1
            box[i][j] = str(num)
            num += 1
            
    cnt -= 1
i -= 1
box[i][j] = str(num)
box[i][j+1] = 'T'
for b in box:
    print(" ".join(b))