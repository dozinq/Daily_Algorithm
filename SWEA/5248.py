import sys
sys.stdin = open('input.txt')

def group(n):
    for i in data[n]:
        if not visited[i]:
            visited[i] = True
            group(i)
    return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    data = [[] for _ in range(N+1)]
    for i in range(0, len(tmp), 2):
        data[tmp[i]].append(tmp[i+1])
        data[tmp[i+1]].append(tmp[i])

    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            group(i)
    print(f'#{tc} {cnt}')

