N = int(input())
S = input()
box = []
for i in range(97, 123):
    box.append([chr(i),0])


cnt = 0
lit = S[0]
i = 0
while N > i:
    
    if S[i] == lit:
        cnt += 1
    else:
        if box[ord(lit)-97][1] < cnt:
            box[ord(lit)-97][1] = cnt
        lit = S[i]
        cnt = 1
    i += 1
if box[ord(lit)-97][1] < cnt:
    box[ord(lit)-97][1] = cnt



cnt = 0
for x in box:
    cnt += x[1]
print(cnt)