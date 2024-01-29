N, M = map(int,input().split())
S = input()
T = input()
import sys

while S.find(T) != -1:
    S = S[:S.rfind(T)] + '#'*M + S[S.rfind(T)+M:]


if M >= 2:
    T21 = T[:M-1] + '#'
    while S.find(T21) != -1:
        S = S[:S.rfind(T21)] + '#'*M + S[S.rfind(T21)+M:]

if M >= 3:
    T31 = T[:M-2] + '##'
    while S.find(T31) != -1:
        S = S[:S.rfind(T31)] + '#'*M + S[S.rfind(T31)+M:]

if M >= 4:
    T41 = T[:M-3] + '###'
    while S.find(T41) != -1:
        S = S[:S.rfind(T41)] + '#'*M + S[S.rfind(T41)+M:]

if M >= 5:
    T51 = T[0] + '####'
    while S.find(T51) != -1:
        S = S[:S.rfind(T51)] + '#'*M + S[S.rfind(T51)+M:]


#     T22 = '#' + T[1:] 
#     while S.find(T22) != -1:
#         S = S[:S.rfind(T22)] + '#'*M + S[S.rfind(T22)+M:]




#     T32 = '##' + T[2:] 
#     while S.find(T32) != -1:
#         S = S[:S.rfind(T32)] + '#'*M + S[S.rfind(T32)+M:]

#     T33 = '#' + T[1:M-1] +'#'
#     while S.find(T33) != -1:
#         S = S[:S.rfind(T33)] + '#'*M + S[S.rfind(T33)+M:]




#     T42 = '###' + T[3:] 
#     while S.find(T42) != -1:
#         S = S[:S.rfind(T42)] + '#'*M + S[S.rfind(T42)+M:]

#     T43 = '##' + T[2:M-1] +'#'
#     while S.find(T43) != -1:
#         S = S[:S.rfind(T43)] + '#'*M + S[S.rfind(T43)+M:]

#     T44 = '#' + T[1:M-2] +'##'
#     while S.find(T44) != -1:
#         S = S[:S.rfind(T44)] + '#'*M + S[S.rfind(T44)+M:]

    


#     T52 = '#' + T[1] + '###'
#     while S.find(T52) != -1:
#         S = S[:S.rfind(T52)] + '#'*M + S[S.rfind(T52)+M:]

#     T53 = '##' + T[2] + '##'
#     while S.find(T53) != -1:
#         S = S[:S.rfind(T53)] + '#'*M + S[S.rfind(T53)+M:]

#     T54 = '###' + T[3] + '#'
#     while S.find(T54) != -1:
#         S = S[:S.rfind(T54)] + '#'*M + S[S.rfind(T54)+M:]

#     T55 = '####' + T[4]
#     while S.find(T55) != -1:
#         S = S[:S.rfind(T55)] + '#'*M + S[S.rfind(T55)+M:]

if S ==  '#'*N:
    print('Yes')
else:
    print('No')