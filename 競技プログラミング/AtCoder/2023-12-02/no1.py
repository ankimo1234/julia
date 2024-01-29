M,D = map(int,input().split())
y, m, d = map(int,input().split())

if d == D:
    if M == m:
        print(str(y+1) + ' 1 1')
    else:
        print(str(y) + ' ' + str(m+1) + ' 1' )
else:
    print(str(y) + ' ' + str(m) + ' ' + str(d+1))