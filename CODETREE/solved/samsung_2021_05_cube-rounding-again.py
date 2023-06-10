import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def rotate_cube(d):
    global cube
    # 우측 방향으로 이동 시
    if d == 0:
        cube = [cube[0], cube[2], cube[3], cube[4], cube[1], cube[5]]
    # 아래 방향으로 이동 시
    elif d == 1:
        cube = [cube[2], cube[1], cube[5], cube[3], cube[0], cube[4]]
    # 좌측 방향으로 이동 시
    elif d == 2:
        cube = [cube[0], cube[4], cube[1], cube[2], cube[3], cube[5]]
    # 위 방향으로 이동 시
    elif d == 3:
        cube = [cube[4], cube[1], cube[0], cube[3], cube[5], cube[2]]
    return

def move_cube():
    global ans, cube_pos, cube_dir
    next_x, next_y = cube_pos[0] + delta[cube_dir][0], cube_pos[1] + delta[cube_dir][1]
    if check_square(next_x, next_y) == False:
        cube_dir = (cube_dir + 2) % 4
        next_x, next_y = cube_pos[0] + delta[cube_dir][0], cube_pos[1] + delta[cube_dir][1]
    cube_pos = (next_x, next_y)
    ans += get_score(cube_pos[0], cube_pos[1])
    rotate_cube(cube_dir)
    if cube[2] > data[cube_pos[0]][cube_pos[1]]:
        cube_dir = (cube_dir + 1) % 4
    elif cube[2] < data[cube_pos[0]][cube_pos[1]]:
        cube_dir = (cube_dir - 1)
        if cube_dir < 0:
            cube_dir = 3
    return

def get_score(x, y):
    tmp_cnt = 0
    stack = [(x, y)]
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    while stack:
        a, b = stack.pop()
        if visited[a][b] == 0:
            tmp_cnt += 1
            visited[a][b] = 1
            for i in range(4):
                nr, nc = a + delta[i][0], b + delta[i][1]
                if check_square(nr, nc) == True:
                    if data[nr][nc] == data[a][b]:
                        stack.append((nr, nc))
    return data[x][y] * tmp_cnt


n, m = map(int, input().split())
data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

# 우, 하, 좌, 상
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 주사위 초기값(전개도 순서대로 임의로 입력. 2번째 인덱스가 아래에 있는 값)
cube = [5, 4, 6, 3, 1, 2]

# 현재 위치, 현재 방향
cube_pos = (0, 0)
cube_dir = 0

ans = 0

for _ in range(m):
    move_cube()

print(ans)