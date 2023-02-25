"""
규칙을 찾아 재귀형식으로 저장된 변수의 값을 증가 시키는 형식으로 답을 구하려 하였으나, 시간 초과.
17070-1 이라는 파일명으로 dp를 구현할 생각이다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def move_pipe(x, y, dir):
    global ans
    if x == (N-1) and y == (N-1):
        ans += 1
        return
    else:
        # 가로 방향이라면,
        if dir == 0:
            # 1. 가로 방향으로
            if data[x][y+1] == 0:
                move_pipe(x, y+1, 0)
            # 2. 대각선 방향으로
            if data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
                move_pipe(x+1, y+1, 2)
        # 세로 방향이라면,
        elif dir == 1:
            # 1. 세로 방향으로
            if data[x+1][y] == 0:
                move_pipe(x+1, y, 1)
            # 2. 대각선 방향으로
            if data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
                move_pipe(x+1, y+1, 2)
        # 대각선 방향이라면,
        else:
            # 1. 가로 방향으로
            if data[x][y+1] == 0:
                move_pipe(x, y+1, 0)
            # 2. 세로 방향으로
            if data[x+1][y] == 0:
                move_pipe(x+1, y, 1)
            # 3. 대각선 방향으로
            if data[x+1][y] == 0 and data[x][y+1] !=1 and data[x+1][y+1] == 0:
                move_pipe(x+1, y+1, 2)
        return

N = int(input())

data = [list(map(int, sys.stdin.readline().split())) + [2] for _ in range(N)]
data.append([2] * (N+1))

ans = 0
move_pipe(0, 1, 0)
print(ans)
