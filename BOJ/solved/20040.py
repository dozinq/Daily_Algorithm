"""
union-find가 생각이 났고, 이를 구현해보았다.
"""

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

import sys
sys.stdin = open('BOJ/input.txt')

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

ans = 0
for i in range(1, m+1):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    if find(node_1) != find(node_2):
        union(node_1, node_2)
    else:
        ans = i
        break

print(ans)