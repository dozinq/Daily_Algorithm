import sys
sys.stdin = open('input.txt')

def way(where, n, dist):
    global ans
    if dist > ans:
        return
    if n == N-1:
        dist += data[where][1]
        ans = min(ans, dist)
    else:
        for i in range(1, N+1):
            if not visited[i] and where != i:
                visited[i] = 1
                way(i, n+1, dist + data[where][i])
                visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = []
    for i in range(0, N+1):
        if i == 0:
            data.append([0]*(N+1))
        else:
            data.append([0] + list(map(int, input().split())))
    visited = [0]*(N+1)
    visited[1] = 1
    ans = 10000
    way(1, 0, 0)
    print(f'#{tc} {ans}')
