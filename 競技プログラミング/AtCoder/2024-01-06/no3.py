from collections import defaultdict
N, Q = map(int,input().split())


cnt = 0
move = defaultdict(list)
x,y = 0,0
query = [input().split() for _ in range(Q)]
for q in query:

    if q[0] == "1":
        cnt += 1
        i = q[1]
        if i == "R":
            x += 1
            
        elif i == "L":
            x -= 1

        elif i == "U":
            y += 1

        elif i == 'D':
            y -= 1

        move[cnt] = [x,y]


    elif q[0] == "2":
        i = int(q[1])
        if cnt > i-1:
            
            place = [1,0]
            place = [l+m for (l,m) in zip(place,move[cnt-i+1])]
        else:
            place = [i-cnt,0]
        print(str(place[0]) + " " + str(place[1]))