import sys
input = sys.stdin.readline

from itertools import accumulate
from bisect import bisect_right
N, Q = map(int,input().split())
R = list(map(int,input().split()))
query = [int(input()) for _ in range(Q)]
R.sort()
accR = list(accumulate(R))


for q in query:
    
    print(bisect_right(accR,q))