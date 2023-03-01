"""
heapq를 쓰지 않고 풀이하려니 되지 않았다.
1753-1 이라는 이름의 파일로 새로 작성하려한다.
"""


import sys
sys.stdin = open('BOJ/input.txt')

def min_route(idx, val):
    global data
    if idx == 0:
        return
    visited[idx] = 1
    next = [10**6, 0]
    for i in range(1, len(data[idx])):
        # 목적지가 자기 자신이 아니라면,
        if i != K:
            data[K][i] = min(data[K][i], data[idx][i] + val)
            if data[K][i] < next[0] and visited[i] == 0:
                next = [data[K][i], i]
    min_route(next[1], next[0])
    return

V, E = map(int, input().split())
K = int(input())
# 최대 거리로 배열을 만들고,
data = [list((10**6) for _ in range(V+1)) for _ in range(V+1)]
# 자기 자신으로 이동하는 간선은 0으로 설정
for i in range(1, V+1):
    data[i][i] = 0
# 입력 값에 따라 간선의 길이를 부여
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    data[u][v] = w

# Dijkstra의 방문 배열
visited = [0] * (V+1)

min_route(K, 0)

for idx in range(1, len(data[K])):
    if data[K][idx] == 10**6:
        print('INF')
        continue
    print(data[K][idx])
    
