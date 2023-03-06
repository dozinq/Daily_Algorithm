"""
조상 노드를 찾는다면, 그때부터 그들의 한 루트씩을 DFS로 탐색 후, ans에 최댓값을 갱신하며 순회.
위상정렬이라는 것을 뒤늦게 깨닫고, 1005-1의 이름으로 새로운 파일 작성.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def DFS(n, cnt):
    global ans
    for i in relation[n][1]:
        if i in essential_lst[1]:
            if i == target:
                ans = max(ans, cnt+val[i-1])
                return
            DFS(i, cnt+val[i-1])
    return

for tc in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().split())

    val = list(map(int, sys.stdin.readline().split()))

    relation = [list(list() for _ in range(2)) for _ in range(N+1)]
    for _ in range(K):
        node_1, node_2 = map(int, sys.stdin.readline().split())
        # 0번째 인덱스에는 부모노드가, 1번째 인덱스에는 자식노드가 위치한다.
        relation[node_2][0].append(node_1)
        relation[node_1][1].append(node_2)

    target = int(input())
    # 조상노드로부터 자식노드를 탐색할때에 불필요한 원소들을 탐색하지 않기 위한 장치
    # 0번째 인덱스에는 조상노드(출발점)만, 1번째 인덱스에는 자식노드만 담는다.
    essential_lst = [[], []]
    stack = [target]
    visited = []
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            for i in relation[tmp][0]:
                # 탐색하는 노드의 부모노드가 없다면(== 조상노드라면), 0번째 인덱스에 추가.
                if len(relation[i][0]) == 0:
                    if i not in essential_lst[0]:
                        essential_lst[0].append(i)
                    continue
                if i not in essential_lst[1]:
                    essential_lst[1].append(i)
                stack.append(i)
    essential_lst[1].append(target)
    ans = val[target-1]
    for i in essential_lst[0]:
        DFS(i, val[i-1])
    print(ans)