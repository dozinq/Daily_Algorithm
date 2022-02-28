import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = [list(map(int, input().split()))for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp_sum = 0
            for k in range(M):
                for l in range(M):
                    tmp_sum += num_lst[i+k][j+l]
            if ans < tmp_sum:
                ans = tmp_sum

    print(f'#{tc} {ans}')