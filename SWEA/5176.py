import sys
sys.stdin = open('input.txt')

def search(node):
    global n
    if node:
        if 2*node <= N:
            search(2*node)
        n += 1
        data[node] += n
        if (2*node)+1 <= N:
            search(2*node+1)
        return data

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [0]*(N+1)
    n = 0
    search(1)
    print(f'#{tc} {data[1]} {data[N//2]}')