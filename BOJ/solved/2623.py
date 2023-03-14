import sys
from collections import deque
sys.stdin = open('BOJ/input.txt')

N, M = map(int, sys.stdin.readline().split())

data = [list() for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tmp)-1):
        data[tmp[i]].append(tmp[i+1])
        cnt[tmp[i+1]] += 1

queue = deque()
for i in range(1, N+1):
    if cnt[i] == 0:
        queue.append(i)

ans_lst = []
visited = [0 for _ in range(N+1)]
while queue:
    tmp = queue.popleft()
    if visited[tmp] == 0:
        visited[tmp] = 1
        ans_lst.append(tmp)
        for j in data[tmp]:
            cnt[j] -= 1
            if cnt[j] == 0:
                queue.append(j)

if len(ans_lst) != N:
    print(0)
else:
    for i in ans_lst:
        print(i)
