"""
한번 분할할 수 있다는 뜻은 곧, 총 edge의 수가 N-2개만 충족시키면 된다고 판단하였고,
이를 union-find, kruskal's algorithm을 이용하여 풀이할 수 있었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(cnt):
    ans = 0
    for node_1, node_2, val in data:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            ans += val
            cnt -= 1
        if cnt == 0:
            return ans

N, M = map(int, input().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
data.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
print(kruskal(N-2))