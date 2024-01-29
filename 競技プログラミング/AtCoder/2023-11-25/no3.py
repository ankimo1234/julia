D = int(input())
route_D = int(D**0.5)
X,Y = 0,0
X = 1 + int(route_D)
close_ans = abs(X**2 + Y**2 - D)
Y = -1
while Y < int(D)+1 and X >= 0:
    Flag = True
    X -= 1
    while Flag:
        Y += 1

        ans = X**2 + Y**2 - D
        close_ans = min(abs(ans),close_ans)
        if ans >= 0:
            Flag=False
print(close_ans)
