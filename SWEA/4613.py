import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    paint_lst = []

    for b in range(1, N-1):
        for r in range(b+1, N):
            tmp_num = 0
            start = 0
            blue, red = b, r
            while start < blue:
                tmp_num += M - lst[start].count('W')
                start += 1
            while blue < red:
                tmp_num += M - lst[blue].count('B')
                blue += 1
            while red < N:
                tmp_num += M - lst[red].count('R')
                red += 1
            paint_lst.append(tmp_num)
    print(f'#{tc} {min(paint_lst)}')
