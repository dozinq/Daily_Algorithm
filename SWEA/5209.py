import sys
sys.stdin = open('input.txt')

def min_sum(num, total):
    global ans

    if ans < total:
        return
    if num == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            min_sum(num+1, total + data[i][num])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    total = 0
    ans = 1500
    min_sum(0, 0)
    print(f'#{tc} {ans}')
