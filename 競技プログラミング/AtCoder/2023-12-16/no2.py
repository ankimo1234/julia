S = input()
T = input()

S1,S2 = S[0],S[1]
T1,T2 = T[0],T[1]

box = ['A','B','C','D','E']

for i,alp in enumerate(box):
    if S1 == alp:
        S1num = i
    if S2 == alp:
        S2num = i
    if T1 == alp:
        T1num = i
    if T2 == alp:
        T2num = i

if S1num > S2num:
    Srange = min(S1num - S2num, S2num + 5 - S1num)

else:
    Srange = min(S2num - S1num, S1num + 5 - S2num)

if T1num > T2num:
    Trange = min(T1num - T2num, T2num + 5 - T1num)

else:
    Trange = min(T2num - T1num, T1num + 5 - T2num)

if Srange == Trange:
    print('Yes')
else:
    print('No')