import sys

sys.stdin = open('input.txt')


def max_edge(num, dist):
    ans_lst.append(dist)
    for n in data[num]:
        if not visited[n]:
            visited[n] = 1
            max_edge(n, dist + 1)
            visited[n] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = [[] for _ in range(N + 1)]

    for _ in range(M):
        node1, node2 = map(int, input().split())
        data[node1].append(node2)
        data[node2].append(node1)

    ans_lst = []
    for i in range(1, N + 1):
        visited = [0] * (N+1)
        visited[i] = 1
        max_edge(i, 1)
    print(f'#{tc} {max(ans_lst)}')