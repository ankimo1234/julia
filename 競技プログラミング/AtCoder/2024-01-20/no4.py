from collections import deque
import sys
H,W,K = map(int,input().split())
box = [input() for _ in range(H)]
cnt = K + 1

for i in range(H):
    xxx = deque()
    xx = 0
    for j in range(W):
        if box[i][j] != "x":
            xxx.append(box[i][j])
            if box[i][j] == ".":
                xx += 1
            if len(xxx) == K:
                cnt = min(cnt,xx)
                l = xxx.popleft()
                if l == ".":
                    xx -= 1
                if cnt == 0:
                    print(0)
                    sys.exit()
        else:
            xxx = deque()
            xx = 0

xxx = 0

for j in range(W):
    yyy = deque()
    yy = 0
    for i in range(H):
        if box[i][j] != "x":
            yyy.append(box[i][j])
            if box[i][j] == ".":
                yy += 1
            if len(yyy) == K:
                cnt = min(cnt,yy)
                l = yyy.popleft()
                if l == ".":
                    yy -= 1
                if cnt == 0:
                    print(0)
                    sys.exit()
        else:
            yyy = deque()
            yy = 0

if cnt > K:
    print(-1)
else:
    print(cnt)