import sys
sys.stdin = open('input.txt')

def find_start(where):              # 재귀보다는 while문으로 해결하려 하였다. (속도)
    visited = [[0]*16 for _ in range(16)]
    stack = []
    stack.append((where[0], where[1]))
    while stack:
        tmp_x, tmp_y = stack.pop()
        if not visited[tmp_x][tmp_y]:
            visited[tmp_x][tmp_y] = 1
            for n in range(4):
                if data[tmp_x+delta[n][0]][tmp_y+delta[n][1]] == 0:
                    stack.append((tmp_x+delta[n][0], tmp_y+delta[n][1]))
                if data[tmp_x+delta[n][0]][tmp_y+delta[n][1]] == 2:
                    return 1
    return 0


for tc in range(1, 11):
    input()
    data = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if data[i][j] == 3:
                goal = (i, j)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    print(f'#{tc} {find_start(goal)}')

