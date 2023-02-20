"""
1년 전 이맘때쯤, DFS와 BFS를 배운 것 같다.
그 당시엔 간단한 개념이지만 코드로 만드려니 어려웠었고, 무작정 코드를 외우려고만 했었다.
진도가 너무 빨랐으니깐 탐색 구현에 지체할 수 없었다. 역시나, 부작용이 있었던 것 같다.
다만, 오랜만에 알고리즘을 짜보는 지금은 더 오래걸리긴 해도 생각하면서 풀이하고 있다.
부족한 부분은 코드 리뷰를 통해 메꿔 나아가려 한다.
print문에서의 언패킹연산자도 개념을 알고 있었지만, 처음 써보았다.
얼른 모든 것이 다 익숙해졌으면 좋겠다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def DFS(node):
    stack = [node]
    visited = []

    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            data[tmp].sort(reverse=True)
            for idx in data[tmp]:
                stack.append(idx)
    return visited


def BFS(node):
    queue = [node]
    visited = []

    while queue:
        tmp = queue.pop(0)
        if tmp not in visited:
            visited.append(tmp)
            data[tmp].sort()
            for idx in data[tmp]:
                queue.append(idx)
    return visited

N, M, V = map(int, input().split())
data = [list() for _ in range(N+1)]

for _ in range(M):
    node = list(map(int, sys.stdin.readline().split()))
    data[node[0]].append(node[1])
    data[node[1]].append(node[0])


print(*DFS(V))
print(*BFS(V))