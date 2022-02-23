import sys
sys.stdin = open('input.txt')

def ans(me, goal):
    stack = [me]
    while stack:
        me = stack.pop()
        if goal in graph[me]:
            return 1
        else:
            for i in graph[me]:
                if i not in visited[me]:
                    visited[me].append(i)
                    stack.append(i)
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    visited = [[] for _ in range(V+1)]

    S, G = map(int, input().split())
    print(f'#{tc} {ans(S, G)}')