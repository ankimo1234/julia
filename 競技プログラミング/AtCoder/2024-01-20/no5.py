import sys
N = int(input())
M = N-1
print(M,flush=True)

for i in range(M):
    print(str(1) + " " + str(i+1),flush=True)

S = input()

if "1" in S:
    print(S.find("1")+1)
else:
    print(N)
sys.exit()