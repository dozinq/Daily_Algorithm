import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 0번째 인덱스는 대각 왼쪽, 1번째 인덱스는 아래쪽, 2번째 인덱스는 대각 오른쪽
memo = list(data[0][:] for _ in range(3))

for i in range(1, N):
    tmp = list(list(float('inf') for _ in range(M)) for _ in range(3))
    for j in range(3):
        for k in range(M):
            if k+1 < M:
                tmp[0][k] = min(memo[1][k+1], memo[2][k+1]) + data[i][k]
            if k-1 >= 0:
                tmp[2][k] = min(memo[0][k-1], memo[1][k-1]) + data[i][k]
            tmp[1][k] = min(memo[0][k], memo[2][k]) + data[i][k]
    memo = tmp

ans = float('inf')
for i in range(3):
    ans = min(ans, min(memo[i]))

print(ans)
