"""
DFS는 재귀가 가장 일반적이고, BFS는 from collections import deque를 통해 popleft()를 사용하는 게 일반적이라고 한다.
다만, 이 문제에서는 재귀로 풀었을때 recursion error를 만날 수 있었기에 따로 함수를 선언해주어야 하였다.
그래서 번거로움을 일단 없애고 while문으로 구현하여 해결할 수 있었다.
"""

import sys
# sys.setrecursionlimit(5000)
sys.stdin = open('BOJ/input.txt')

# RecursionError 발생. => sys.setrecursionlimit()으로 해결 가능하긴 하나, while문으로 작성하여 해결.
# def DFS(node):
#     global visited
#     visited[node] = 1
#     for idx in data[node]:
#         if visited[idx] == 0:
#             DFS(idx)

def DFS(node):
    global visited
    stack = [node]

    while stack:
        tmp = stack.pop()
        if visited[tmp] == 0:
            visited[tmp] = 1
            for i in data[tmp]:
                if visited[i] == 0 and i not in stack:
                    stack.append(i)
    return

N, M = map(int, input().split())
data = [list() for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    data[u].append(v)
    data[v].append(u)

visited = [0 for _ in range(N+1)]

cnt = 0
for idx in range(1, N+1):
    if visited[idx] == 0:
        DFS(idx)
        cnt += 1

print(cnt)