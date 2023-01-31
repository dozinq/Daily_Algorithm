import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
tmp = []

def dfs():
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return

    for i in range(1, N+1):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()