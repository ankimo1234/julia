N, X = map(int,input().split())
S = input().split()
cnt = 0
for x in S:
    if int(x) <= X:
        cnt += int(x)
print(cnt)