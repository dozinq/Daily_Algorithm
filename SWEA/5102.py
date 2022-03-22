# cnt 변수 써서 별 짓 다하다가 최단경로 수를 못찾고 카운트는 늘어만 가길래,
# BFS 개념 확립하고 다시 처음부터 풀어보았습니다..

import sys
sys.stdin = open('input.txt')

def BFS(num):                                   # BFS로 너비우선탐색 이용해야한다는 것을 깨달았습니다!
    visited = [0]*(V+1)                         # cnt변수로 while문이 실행될때마다 1씩 증가하게 해주었더니 당연히 오류를 겪었고,
                                                # visited를 빈 리스트가 아닌, 목표지점까지의 길이를 기록할 수 있도록 하였습니다.
    queue = []                                  # queue를 이용하자!
    queue.append(num)
    while queue:
        tmp = queue.pop(0)
        for i in data[tmp]:
            if visited[i] == 0:
                visited[i] = visited[tmp] + 1
                queue.append(i)
            if i == G:
                return visited[i]
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[] for _ in range(V+1)]
    for _ in range(E):
        tmp = list(map(int, input().split()))
        data[tmp[0]].append(tmp[1])
        data[tmp[1]].append(tmp[0])
    S, G = map(int, input().split())

    print(f'#{tc} {BFS(S)}')

