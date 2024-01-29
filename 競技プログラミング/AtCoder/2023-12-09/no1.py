N = int(input())
A = list(map(int,input().split()))
P = list(map(int,input().split()))
remove_box = []
newP = []
for i,p in enumerate(P):
    if i + 2 == p:
        remove_box.append(p)
    elif remove_box.count(p) > 0:
        remove_box.append(p)
    else:
        newP.append(p)
P = newP


# if P[-1] == 0:
#     if A[0] < 0:
#         print('-')
#     elif A[0] == 0:
#         print(0)
#     elif A[0] > 0:
#         print('+')
# elif P[-1] > 0:
#     print('+')
# elif P[-1] < 0:
#     print('-')

A_num = sum(A)
print(P)
for j in range(10000):
    for i,p in enumerate(P):
        A[p-1] = A[i+1] + A[p-1]
diff_num = sum(A) - A_num
print(diff_num)
if diff_num == 0 or P.count(1) == 0:
    if A[0] < 0:
        print('-')
    elif A[0] == 0:
        print(0)
    elif A[0] > 0:
        print('+')
elif diff_num < 0:
    print('-')

elif diff_num > 0:
    print('+')