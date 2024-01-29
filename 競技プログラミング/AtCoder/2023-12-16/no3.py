def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


N = int(input())
n = base10int(N*2+1,3)


box = [1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111,111111111111]
ans = []
for x in box:
    for xx in box:
        for xxx in box:
            ans.append(x+xx+xxx)
ans = set(ans)
ans = sorted(ans)
print(ans[N-1])