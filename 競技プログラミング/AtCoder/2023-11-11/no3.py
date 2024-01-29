N, Q = map(int,input().split())
S = input()
box = [[0]]
cnt = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt += 1
    box.append([cnt])

for _ in range(Q):
    l,r = map(int,input().split())
    x = box[r-1][0] - box[l-1][0]
    print(x)

