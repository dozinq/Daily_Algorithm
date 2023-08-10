from collections import deque
import sys
sys.stdin = open('BOJ/input.txt')

def check_square(a, b):
    if 0 <= a < N and 0 <= b < M:
        return True
    return False

def dfs(row, col):
    for d in delta:
        nr, nc = row + d[0], col + d[1]
        if check_square(nr, nc) == True:
            if data[nr][nc] == 1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[row][col] + 1
                    dfs(nr, nc)
                elif visited[nr][nc] > visited[row][col] + 1:
                    visited[nr][nc] = visited[row][col] + 1
                    dfs(nr, nc)
    return

def bfs():
    queue = deque((0, 0))
    while queue:
        r, c = queue.popleft()
        if visited[r][c] == 0:
            visited[r][c] = 1
            for d in delta:
                if visited[r+d[0]][c+d[1]] == 0:
                    queue.append((r+d[0], c+d[1]))
                elif visited[r+d[0]][c+d[1]]

    return

N, M = map(int, input().split())

data = [list(map(int, input())) for _ in range(N)]

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [list(0 for _ in range(M)) for _ in range(N)]
visited[0][0] = 1
bfs()
print(visited[N-1][M-1])