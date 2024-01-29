import sys

def input():
    return sys.stdin.readline()[:-1]

def main():
    H, W = map(int,input().split())
    box = []
    for i in range(H):
        box.append(list(map(str,input())))

    def check(i,j,S):
        S[i][j] = '.'
        around = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for height, widht in around:
            if  0 <= i+height < H and 0 <= j+widht < W:
                if S[i+height][j+widht] == '#':
                    check(i+height, j+widht, S)
        
    cnt = 0
    for i in range(H):
        for j in range(W):
            if box[i][j] == '#' :
                check(i,j,box)
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()