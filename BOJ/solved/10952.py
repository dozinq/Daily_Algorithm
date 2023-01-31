import sys
A = 1
B = 1

while (A != 0 or B != 0) :
    A, B = map(int, sys.stdin.readline().split())
    if A ==0 and B==0 :
        break
    print(A + B)
