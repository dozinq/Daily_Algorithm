"""
dp를 사용하여 빠른 수행시간으로 문제를 풀어보았다.
dp는 논리적 순서만 지켜서 설계해준다면 알아서 규칙에 따라 계산해주는게 좀 신기하다고도 생각된다.
해당 배열을 순차적으로 순회하면서 경우의 수를 모두 체크해주는 로직이다.
또한 방향도 상관있으므로 배열을 세 개를 준비해두었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def move_pipe():
    global memo_row, memo_col, memo_diag
    for x in range(1, N):
        for y in range(1, N):
            if data[x][y-1] == 0 and data[x-1][y] ==0 and data[x][y] == 0:
                memo_diag[x][y] = memo_row[x-1][y-1] + memo_col[x-1][y-1] + memo_diag[x-1][y-1]
            if data[x][y] == 0:
                memo_row[x][y] = memo_row[x][y-1] + memo_diag[x][y-1]
            if data[x][y] == 0:
                memo_col[x][y] = memo_col[x-1][y] + memo_diag[x-1][y]
    return

N = int(input())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

memo_row = [list(0 for _ in range(N)) for _ in range(N)]
for idx in range(1, N):
    if data[0][idx] != 1:
        memo_row[0][idx] = 1
    else:
        break
memo_col = [list(0 for _ in range(N)) for _ in range(N)]
memo_diag = [list(0 for _ in range(N)) for _ in range(N)]

move_pipe()
print(f'{memo_row[N-1][N-1] + memo_col[N-1][N-1] + memo_diag[N-1][N-1]}')
