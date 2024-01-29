import sys
import fractions
from math import gcd
sys.setrecursionlimit(10**6)

H ,W = map(int,input().split())

grids = ['']*H
belongings = [[0]*W for _ in range(H)]
for i in range(H):
    grids[i] = input()


def check(height,width):
    if belongings[height][width] == cnt:
        pass
    else:
        belongings[height][width] = cnt
        if width < W-1:
            if grids[height][width+1] == '#':
                check(height,width+1)
        if width > 0:
            if grids[height][width-1] == '#':
                check(height,width-1)
        if height < H-1:
            if grids[height+1][width] == '#':
                check(height+1,width)
        if height > 0:
            if grids[height-1][width] == '#':
                check(height-1,width)

cnt = 0
for i in range(H):
    for j in range(W):
        if belongings[i][j] == 0:
            if grids[i][j] == '#':
                cnt += 1
                check(i,j)
                
            else:
                pass


ans = 0
CNT = 0
for i in range(H):
    for j in range(W):
        if belongings[i][j] == 0:
            CNT += 1
            around = set()
            if i > 0:
                if belongings[i-1][j]:
                    around.add(belongings[i-1][j])
            if i < H-1:
                if belongings[i+1][j]:
                    around.add(belongings[i+1][j])
            if j > 0:
                if belongings[i][j-1]:
                    around.add(belongings[i][j-1])
            if j < H-1:
                if belongings[i][j+1]:
                    around.add(belongings[i][j+1])
            ans += (cnt-len(around)+1)

x = gcd(ans,CNT)
ans = int(ans/x)
CNT = int(CNT/x)
mod = 998244353
n = pow(CNT, -1, mod)
print(ans * n % mod)