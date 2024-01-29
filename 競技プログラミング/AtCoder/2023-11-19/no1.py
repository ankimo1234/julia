N = int(input())
S = input()


cnt,CNT = 0,0
for i in range(N-1):
    if S[i] == '>':
        CNT += 1
        cnt += CNT
    else:
        CNT = 0
print(cnt)