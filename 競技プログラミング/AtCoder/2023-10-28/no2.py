N = input()
x = N
while True:
    if int(x[0]) * int(x[1]) == int(x[2]):
        print(x)
        break
    else:
        x = str(int(x)+ 1)