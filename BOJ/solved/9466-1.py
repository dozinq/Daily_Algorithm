import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit(1000000)

def dfs(num):
    global ans
    visited[num] = 1
    team_lst.append(num)
    next = data[num]
    if visited[next] == 1:
        if next in team_lst:
            ans += len(team_lst) - team_lst.index(next)
        return
    else:
        dfs(next)

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    data = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(n+1)]

    ans = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            team_lst = []
            dfs(i)

    ans = n - ans
    print(ans)