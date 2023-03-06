"""
위상 정렬을 이용한 풀이 방법이다.
이전의 essential_lst라는 이름으로 필요 노드만 탐색하도록 하였는데,
그것이 되려 시간이 더 오래 걸리고 메모리도 더 차지하여 결국 방법을 바꾸어보았다.
"""

import sys
from collections import deque
sys.stdin = open('BOJ/input.txt')

for tc in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().split())

    data = list(map(int, sys.stdin.readline().split()))

    sons = [list() for _ in range(N+1)]
    wei = [0 for _ in range(N+1)]
    for _ in range(K):
        node_1, node_2 = map(int, sys.stdin.readline().split())
        sons[node_1].append(node_2)
        wei[node_2] += 1

    target = int(input())

    grp_lst = []
    for i in range(1, N+1):
        if wei[i] == 0:
            grp_lst.append(i)

    ans_lst = data[:]
    queue = deque(grp_lst[:])
    while queue:
        elem = queue.popleft()
        for i in sons[elem]:
            wei[i] -= 1
            ans_lst[i-1] = max(ans_lst[i-1], ans_lst[elem-1] + data[i-1])
            if wei[i] == 0:
                queue.append(i)

    print(ans_lst[target-1])