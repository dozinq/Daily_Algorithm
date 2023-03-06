"""
DFS를 이용하여 python3로는 시간초과 이슈가 있어서, pypy 인터프리터로 제출하였다.
되도록이면 pypy를 사용하지 않으려고 하는데, 더 이상 시간을 줄이는 것은 목적에 맞지 않다고 생각되었다.
앞으로도 간단한 함수는 lambda로 대체하려 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

# lambda 식으로 대체
# def cha_to_num(cha):
#     return ord(cha) - 65

def DFS(a, b, cnt):
    global ans
    for d in delta:
        if 0 <= a+d[0] < R and 0 <= b+d[1] < C:
            if visited[data[a+d[0]][b+d[1]]] == 0:
                visited[data[a+d[0]][b+d[1]]] = 1
                DFS(a+d[0], b+d[1], cnt+1)
                visited[data[a+d[0]][b+d[1]]] = 0
    ans = max(ans, cnt)
    return

# 첫번째 풀이 방법. -> 시간 초과
# def DFS(a, b, cnt):
#     global ans
#     if visited[data[a][b]] == 0:
#         visited[data[a][b]] = 1
#         for d in delta:
#             if 0 <= a+d[0] < R and 0 <= b+d[1] < C:
#                 DFS(a+d[0], b+d[1], cnt+1)
#         visited[data[a][b]] = 0
#     ans = max(ans, cnt)
#     return

R, C = map(int, input().split())
data = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().strip())) for _ in range(R)]
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [0] * 26
visited[data[0][0]] = 1

ans = 0
DFS(0, 0, 1)
print(ans)