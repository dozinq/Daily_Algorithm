import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    ans = len(A)
    i = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            ans -= len(B)-1
            i += len(B)-1
        i += 1

    print(f'#{tc} {ans}')