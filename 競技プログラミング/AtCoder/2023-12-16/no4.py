from collections import defaultdict

N = int(input())
d = defaultdict(list)
for i in range(N-1):
    A,B = map(int,input().split())
    
    d[A] += [str(B)]


ans = [N]




dd = [1]*(N)
print(dd)
ans = []
for k,x in reversed(sorted(d.items())):
    print(k,x)
    
    cnt = 1
    for xx in x:
        xx = int(xx)
        if k == 1:
            ans.append(dd[xx-1])
        else:
            
            cnt += dd[xx-1]
    dd[k-1] = cnt
    
print(dd)
print(ans)
x = 0
ans.sort()
ans.pop(-1)
cnt = 0
for x in ans:
    cnt += x
print(x+1)