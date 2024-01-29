
S = input()
l = len(S)
box = [0]*26

for i in range(l):
    box[ord(S[i])-97] += 1
max_cnt = max(box)
print(chr(box.index(max_cnt)+97))
