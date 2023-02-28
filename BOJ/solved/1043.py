"""
단순한 구현을 하였지만, 오류를 범했다고 하였다.
그래서 탐색을 구현하여 해결할 수 있었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def not_truman():
    global data, stack

    while stack:
        truth = stack.pop()
        data[truth] = 1
        for i in graph[truth]:
            if data[i] == 0:
                stack.append(i)
                not_truman()
    return

N, M = map(int, input().split())
data = [0 for _ in range(N+1)]
graph = [list() for _ in range(N+1)]

tmp_lst = list(map(int, input().split()))
for idx in range(1, len(tmp_lst)):
    data[tmp_lst[idx]] = 1
    
all_party = []
stack = []
for idx in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tmp)):
        if tmp[0] >= 2:
            for j in range(1, len(tmp)):
                if tmp[i] != tmp[j]:
                    graph[tmp[i]].append(tmp[j])
        if data[tmp[i]] == 1:
            for j in range(1, len(tmp)):
                if data[tmp[j]] == 0 and tmp[j] not in stack:
                    stack.append(tmp[j])
    all_party.append(tmp)

not_truman()
ans = 0
for party in all_party:
    flag = 0
    for i in range(1, len(party)):
        if data[party[i]] == 1:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)