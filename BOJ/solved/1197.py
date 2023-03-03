"""
Kruskal's Algorithm과 Union-Find에 대해 다시 한번 공부해 볼 수 있었다.
또한 이를 같이 혼합하여 사용한다는 것에 많은 중요성을 느낄 수 있었따.
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
    global ans
    for node_1, node_2, val in data:
        if cnt == 0:
            break
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            ans += val
            cnt -= 1
    return

V, E = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
data.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]
ans = 0
kruskal(V-1)
print(ans)
