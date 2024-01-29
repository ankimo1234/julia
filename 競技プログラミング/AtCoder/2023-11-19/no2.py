# 1 x
# 1 1 1 x
# 1 1 x (k = x-1)
# 1 1 1 x y z
# 1 x y
# 1 1 x y
# 1 100 100 , k=99


#　自分のターンの初めに１の個数が奇数かつ１以外の個数が奇数　＝＝　ｋはすべて
#　自分のターンの初めに１の個数が偶数かつ１以外の個数が奇数　＝＝　ｋはすべて


N = int(input())
A = list(map(int,input().split()))

num1 = A.count(1)
max_num = max(A)
nummax = A.count(max_num)

if N == 1:
    print(-1)
elif N % 2 == 0 and N == num1:
    print(0)

else:
    if num1 != 0 and ((N-num1)%2 == 1 or (N != num1 and num1 % 2 == 0)):
        print(-1)
    else:
        num1 += nummax*2
        N += nummax
        if N % 2 == 0 and N == num1:
            print(0)
        elif (N-num1)%2 == 1 or (N != num1 and num1 % 2 == 0):
            print(max_num-1)
        else:
            print(0)