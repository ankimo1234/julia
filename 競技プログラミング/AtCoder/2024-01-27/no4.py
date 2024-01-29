
from itertools import accumulate
N,M = map(int,input().split())
X = list(map(int,input().split()))



range_list = [0]*N
x0 = 0
for x in X:
    if x0 == 0:
        x0 = x
        continue
    else:
        i = min(x0,x)-1
        j = max(x0,x)-1
        m = j-i
        n = N-(j-i)
        range_list[0] += m
        range_list[i] += (n-m)
        range_list[j] += m-n
        x0 = x

print(min(list(accumulate(range_list))))