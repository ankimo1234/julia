S = input()
i = 0
Flag = True
while Flag:
    if i + 3 >= len(S):
        Flag = False
    # print(S[i:i+3])
    if S[i:i+3] == 'ABC':
        S = S[:i] + S[i+3:]
        # print(S)
        try:
            if S[i] == 'B':
                S[i-1]
                i -= 1
        except:
            pass
        try:
            if S[i] == 'C':
                S[i-2]
                i -= 2
        except:
            pass
    else:
        i += 1
print(S)