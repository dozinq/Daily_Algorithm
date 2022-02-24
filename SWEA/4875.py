import sys
sys.stdin = open('input.txt')

def maze(i, j):
    stack = [(i, j)]
    while stack:
        (i, j) = stack.pop()
        for arrow in range(4):
            if 0 <= i+dr[arrow] < N and 0 <= j+dc[arrow] < N:
                if data[i+dr[arrow]][j+dc[arrow]] == 3:
                    return 1
                elif (i+dr[arrow], j+dc[arrow]) not in visited and data[i+dr[arrow]][j+dc[arrow]] == 0:
                    stack.append((i+dr[arrow], j+dc[arrow]))
                    visited.append((i+dr[arrow], j+dc[arrow]))
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start_i = i
                start_j = j

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = []

    print(f'#{tc} {maze(start_i, start_j)}')