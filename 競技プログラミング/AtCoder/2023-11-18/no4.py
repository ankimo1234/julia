N,M = map(int,input().split())
A = list(map(int,input().split()))

box = [0]*N
top_cnt = 0
current_top = 1

for x in A:
    box[x-1] += 1
    if current_top != x:
        if box[x-1] > top_cnt:
            top_cnt += 1
            current_top = x
        
        elif box[x-1] == top_cnt:
            if current_top > x:
                current_top = x

    else:
        top_cnt += 1
    print(current_top)
