import sys
sys.stdin = open('input.txt')

def sub_tree(node):
    global ans
    if node:
        sub_tree(tree[node][0])
        sub_tree(tree[node][1])
        ans += 1

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0]*2 for _ in range(E+2)]
    for i in range(E):
        if tree[data[2*i]][0] > 0:
            tree[data[2*i]][1] = data[2*i+1]
        else:
            tree[data[2*i]][0] = data[2*i+1]
    ans = 0
    sub_tree(N)

    print(f'#{tc} {ans}')