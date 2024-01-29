import sys
S = input()
l = len(S)
n = 65
if S[0] == "A":
    n = 65
elif S[0] == "B":
    n = 66
elif S[0] == "C":
    n = 67

for i in range(l):
    if S[i] == " ":
        pass
    elif S[i] == chr(n):
        pass
    elif S[i] == chr(n+1):
        n += 1
    elif S[i] == chr(n+2):
        n += 2
    else:
        print("No")
        sys.exit()
print("Yes")