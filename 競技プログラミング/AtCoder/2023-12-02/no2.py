N, S, M, L = map(int,input().split())

s = 0
m = 0
l = 0
ans = 10*L
# N = 6*s + 8*m + 12*l
ll = N /12
if ll != int(ll):
    ll += 1
    ll = int(ll)

for l in range(ll+1):
    for m in range(14):
        Flag = False
        s = (N - 12*l - 8*m)/6

        if s < 0:
            Flag = True
        if s != int(s):
            s += 1
        s = int(s)
        if Flag == True:
            s = 0

        price = S*s + M*m + L*l

        ans = min(price,ans)

        if Flag == True:
            break
print(ans)


