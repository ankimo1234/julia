N = int(input())
D = input().split()
cnt = 0
for i in range(1,N+1):
    for d in range(1,int(D[i-1])+1):
        length = len(str(i) + str(d)) 
        x = str(i)[0]
        if str(i).count(x) + str(d).count(x) == length:
            cnt += 1
            
print(cnt)