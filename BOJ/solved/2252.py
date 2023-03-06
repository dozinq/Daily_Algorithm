"""
처음엔 union-find라고 생각했는데, 오류가 생길 것이라고 생각되었고,
해당 노드보다 큰 노드와 작은 노드를 따로 저장하고, DFS를 수행하면 될 것으로 판단되었다.
"""
import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit(100000)

def finder(x):
    if len(taller[x]) > 0:
        for tall_node in taller[x]:
            if visited[tall_node] == 0:
                finder(tall_node)
    if visited[x] == 0:
        visited[x] = 1
        ans.append(x)
        if len(smaller[x]) > 0:
            for small_node in smaller[x]:
                if visited[small_node] == 0:
                    finder(small_node)

N, M = map(int, sys.stdin.readline().split())

taller = [list() for _ in range(N+1)]
smaller = [list() for _ in range(N+1)]
for _ in range(M):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    taller[node_2].append(node_1)
    smaller[node_1].append(node_2)

visited = [0 for _ in range(N+1)]
ans = []
for i in range(1, N+1):
    finder(i)
print(*ans)

"""
-코드 리뷰-
: 이는 '위상 정렬'이라는 개념을 활용한 문제라고 한다. 개념에 대해서는 README에 적을 것이며,
이를 다음의 코드로도 해결할 수 있다고 하여 작성해보겠다.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
ans = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

# 가장 위에 아무것도 없는 요소를 추가한다.
for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

# 큐를 돌면서 그 다음 순위의 노드를 저장할 수 있도록 한다.
while queue:
    tmp = queue.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*ans)
"""