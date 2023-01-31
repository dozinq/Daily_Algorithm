import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    tmp = ''
    n = 0.5
    while(N > 0):
        if N >= n:
            N -= n
            tmp += '1'
        else:
            tmp += '0'
        if len(tmp) >= 13:
            break
        n *= 0.5

    if len(tmp) >= 13:
        tmp = 'overflow'
    print(f'#{tc} {tmp}')