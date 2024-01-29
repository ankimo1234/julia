S = input()
ans = ''
for i in range(len(S)):
    ans += S[i]
    if i != len(S)-1:
        ans += ' '
print(ans)