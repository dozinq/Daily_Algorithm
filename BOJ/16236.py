import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def search_shark_and_fish():
    fish_pos = [list() for _ in range(7)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 9:
                shark_pos = (i, j)
            elif 0 < data[i][j]:
                fish_pos[data[i][j]].append((i, j))
    return shark_pos, fish_pos

def eat_fish():
    tmp_cnt = 0
    for i in range(1, size+1):
        if len(lst[i]) > 0:
            tmp_cnt += len(lst[i])
            for j in range(len(lst[i])):
                get_dist(i, j, 0)
    if tmp_cnt == 1:
        pass
    return

def get_dist(a, b, cnt):
    visited = [list(0 for _ in range(N)) for _ in range(N)]
    stack = [(a, b)]
    while stack:
        x, y = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
            for d in range(4):
                new_x, new_y = x + delta[d][0], y + delta[d][1]
                if check_square(new_x, new_y) == True:
                    

    return

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

size = 2
pos, lst = search_shark_and_fish()

flag = 0
while True:
    pass
