"""
오류 발생.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

data = []
for _ in range(N):
    data.append(list(map(str, sys.stdin.readline().split())))

delta = ((1, 0, -1, 0), (0, 1, 0, -1))
bar_lst = set()
ans = 1
for i in range(N):
    for j in range(N):
        if data[i][j] == 'T':
            for d in range(4):
                for k in range(1, N):
                    if 0 <= i + (k*delta[0][d]) < N and 0 <= j + (k*delta[1][d]) < N:
                        if data[i+(k*delta[0][d])][j+(k*delta[1][d])] == 'S':
                            # 바로 옆에 학생이 있는 경우
                            if k == 1:
                                ans = 0
                                break
                            else:
                                bar_lst.add((i+((k-1)*delta[0][d]), j+((k-1)*delta[1][d])))

print('NO') if ans == 0 or len(bar_lst) > 3 else print('YES')
