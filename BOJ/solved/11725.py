"""
처음엔 재귀 형식으로 풀려고 했었다. 그러나 limit을 조정해주지 않으면 풀 수가 없었고,
while 형식으로 바꾸어 설계하였다. 또한, 시간을 최소화하기 위해 stack에 추가하기 전에 조건문을 상세히 설정해주었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')
# sys.setrecursionlimit = 10000

def DFS(node):
    global visited
    stack = [node]

    while stack:
        tmp = stack.pop()
        for idx in data[tmp]:
            if visited[idx] == 0 and idx not in stack:
                visited[idx] = tmp
                stack.append(idx)

    # for idx in data[node]:
    #     if visited[idx] == 0:
    #         visited[idx] = node
    #         DFS(idx)
    return

N = int(input())

data = [list() for _ in range(N+1)]

for _ in range(N-1):
    tmp = list(map(int, sys.stdin.readline().split()))
    data[tmp[0]].append(tmp[1])
    data[tmp[1]].append(tmp[0])

visited = [0] * (N+1)
# visited[1] = 1

DFS(1)

for i in range(2, N+1):
    print(visited[i])
