import sys
sys.stdin = open('input.txt')

def search(node):
    if node*2 <= N:
        tree[node] += search(node*2)
    if (node*2)+1 <= N:
        tree[node] += search((node*2)+1)
    return tree[node]

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        tmp_lst = list(map(int, input().split()))
        tree[tmp_lst[0]] = tmp_lst[1]
    print(f'#{tc} {search(L)}')