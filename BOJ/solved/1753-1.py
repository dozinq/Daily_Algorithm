"""
sys.stdin.readline()을 쓰지 않고 풀이하려니 계속 시간 초과 오류가 발생했던 것이다.
또한 heapq에 대한 많은 이해를 얼른 습득해야겠다.
"""

import sys, heapq
sys.stdin = open('BOJ/input.txt')

def dijkstra(node):
    ans[node] = 0
    queue = []
    heapq.heappush(queue, [0, node])

    while queue:
        val, idx = heapq.heappop(queue)
        if ans[idx] < val:
            continue
        for num, wei in data[idx]:
            if ans[num] > val + wei:
                ans[num] = val + wei
                heapq.heappush(queue, [val + wei, num])
    return

V, E = map(int, input().split())
K = int(input())
INF = float('inf')

data = [list() for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    data[u].append([v, w])

ans = [INF for _ in range(V+1)]
dijkstra(K)
for idx in range(1, V+1):
    if ans[idx] == INF:
        print('INF')
    else:
        print(ans[idx])
