"""
알고리즘을 모르고 이 문제를 풀려고 했다가는 많은 시행착오를 마주하게 된다.
다익스트라 알고리즘은 한번 배운적이 있으나, 이 문제를 통해 더 배우게 되는 것 같다.
재귀의 벽에 막혀 많은 실패를 마주치다가 억지로라도 while문으로 변형하여 제출하였다.
많은 감정의 변화가 있었지만, 그래도 나를 더욱 성장시켜준다고 생각하고 좋게 받아들이기로 했다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def dijkstra(num):
    global visited, ans
    # 무한루프 현상이 발생하여 디버그해보니, min의 0인덱스가 node에 들어오게 되는 현상이 반복되었다.
    # if node == 0:
    #     return
    # min 이란, 각 노드를 순회할 때마다 최소값을 저장하여 유망한 다음 순회 노드를 찾으려는 수단이다.
    node = num
    next = [100000001, node]
    while node:
        visited[node] = 1
        next = [100000001, 0]
        for idx in range(1, N+1):
            # 만약, 현재 저장되어 있는 값이 새로운 효율적인 경로를 찾는다면 값을 변경해준다.
        # if ans[idx] > data[node][idx] + ans[node]:
        #     ans[idx] = data[node][idx] + ans[node]
            if idx != node:
                ans[idx] = min(ans[idx], data[node][idx] + ans[node])
                # 아직 방문하지 않은 노드들 중에,
                if visited[idx] == 0:
                    # 최소값을 저장한다.
                    if next[0] > ans[idx]:
                        next = [ans[idx], idx]
        node = next[1]

    # for idx in range(1, N+1):
    #     # 만약, 현재 저장되어 있는 값이 새로운 효율적인 경로를 찾는다면 값을 변경해준다.
    #     # if ans[idx] > data[node][idx] + ans[node]:
    #     #     ans[idx] = data[node][idx] + ans[node]
    #     if idx != node:
    #         ans[idx] = min(ans[idx], data[node][idx] + ans[node])
    #         # 아직 방문하지 않은 노드들 중에,
    #         if visited[idx] == 0:
    #             # 최소값을 저장한다.
    #             if next[0] > ans[idx]:
    #                 next = [ans[idx], idx]
    # # 최솟값의 인덱스를 방문한다.
    # dijkstra(next[1])
    return

N = int(input())

tmp = []
for _ in range(int(input())):
    tmp.append(list(map(int, sys.stdin.readline().split())))

data = [list(100000001 for _ in range(N+1)) for _ in range(N+1)]
for idx in tmp:
    data[idx[0]][idx[1]] = min(data[idx[0]][idx[1]], idx[2])

start, end = map(int, input().split())

visited = [0 for _ in range(N+1)]

ans = data[start].copy()

if start == end:
    print(0)
else:
    dijkstra(start)
    print(ans[end])
