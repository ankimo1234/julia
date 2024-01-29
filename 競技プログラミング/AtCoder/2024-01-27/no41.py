
import numpy as np

N,M = map(int,input().split())
X = np.array(list(map(int,input().split())))
X_diff = np.diff(X)


range_list = [0]*N
range_list = np.array(range_list)
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
        
        range_list[i:j] += n
        range_list[:i] += m
        range_list[j:] += m
        x0 = x

print(min(range_list))