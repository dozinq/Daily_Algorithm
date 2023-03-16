"""
간단한 문제를 어렵게 생각했다.
코드 리뷰를 통해 다시 빠르게 풀이하는 방법을 익혀야겠다.
"""

import sys
from itertools import combinations
sys.stdin = open('BOJ/input.txt')

def seek():
    s_flag = 0
    for t in teacher_lst:
        if s_flag == 1:
            break
        for d in delta:
            if s_flag == 1:
                break
            for k in range(N):
                next_x, next_y = t[0] + (k*d[0]), t[1] + (k*d[1])
                if 0 <= next_x < N and 0 <= next_y < N:
                    if data[next_x][next_y] == 'O':
                        break
                    elif data[next_x][next_y] == 'S':
                        s_flag = 1
                        break
    return s_flag


N = int(input())

data = []
for _ in range(N):
    data.append(list(map(str, sys.stdin.readline().split())))

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

bar_lst = set()
teacher_lst = []
ans = 1
for i in range(N):
    for j in range(N):
        if data[i][j] == 'T':
            teacher_lst.append((i, j))
        elif data[i][j] == 'S':
            for d in range(4):
                if 0 <= i + delta[d][0] < N and 0 <= j + delta[d][1] < N:
                    if data[i + delta[d][0]][j + delta[d][1]] == 'T':
                        ans = 0
        elif data[i][j] == 'X':
            bar_lst.add((i, j))

if ans == 0:
    print('NO')
elif len(bar_lst) < 3:
    print('YES')
else:
    for i in list(combinations(bar_lst, 3)):
        for j in range(3):
            data[i[j][0]][i[j][1]] = 'O'
        ans = seek()
        if ans == 0:
            break
        else:
            for j in range(3):
                data[i[j][0]][i[j][1]] = 'X'
    if ans == 0:
        print('YES')
    elif ans == 1:
        print('NO')