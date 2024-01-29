import sys
sys.setrecursionlimit(10**6)

H, W = map(int,input().split())
box = []
for i in range(H):
    lines = []
    line = input()
    for j in range(W):
        lines.append([line[j],0])
    box.append(lines)
    
def check(i,j):
    box[i][j][1] = 1
    try:
        if i-1 >= 0 and j-1 >= 0:
            if box[i-1][j-1][0] == '#' and box[i-1][j-1][1] == 0:
                check(i-1,j-1)
    except:
        pass

    try:
        if i-1 >= 0:
            if box[i-1][j][0] == '#' and box[i-1][j][1] == 0:
                check(i-1,j)
    except:
        pass

    try:
        if i-1 >= 0 and j+1 <= W:
            if box[i-1][j+1][0] == '#' and box[i-1][j+1][1] == 0:
                check(i-1,j+1)
    except:
        pass

    try:
        if j-1 >= 0:
            if box[i][j-1][0] == '#' and box[i][j-1][1] == 0:
                check(i,j-1)
    except:
        pass

    try:
        if j+1 <= W:
            if box[i][j+1][0] == '#' and box[i][j+1][1] == 0:
                check(i,j+1)
    except:
        pass    

    try:
        if i+1 <= H and j-1 >= 0:
            if box[i+1][j-1][0] == '#' and box[i+1][j-1][1] == 0:
                check(i+1,j-1)
    except:
        pass

    try:
        if i + 1 <= H:
            if box[i+1][j][0] == '#' and box[i+1][j][1] == 0:
                check(i+1,j)
    except:
        pass

    try:
        if i+1 <= H and j+1 <= W:
            if box[i+1][j+1][0] == '#' and box[i+1][j+1][1] == 0:
                check(i+1,j+1)
    except:
        pass

cnt = 0
for i in range(H):
    for j in range(W):
        if box[i][j][0] == '#' and box[i][j][1] == 0:
            check(i,j)
            cnt += 1
print(cnt)