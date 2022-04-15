import sys
sys.stdin = open('input.txt')

def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find(x, y):
    return get_parent(x) == get_parent(y)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: -(x[2]))
    parent = [i for i in range(V + 1)]

    ans = 0
    while data:
        a, b, c = data.pop()
        if not find(a, b):
            union_parent(a, b)
            ans += c

    print(f'#{tc} {ans}')
