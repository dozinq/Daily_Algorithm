import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit(1000000)

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b
        return 0
    else:
        return 1

def dfs(num):
    global ans
    visited[num] = 1
    next = data[num]
    if union(num, next) == 0 and visited[next] == 0:
        team_lst.append(next)
        dfs(next)
    else:
        if visited[next] == 1:
            for team in range(len(team_lst)):
                if team_lst[team] == next:
                    ans += len(team_lst) - team
                    break

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    data = [0] + list(map(int, sys.stdin.readline().split()))

    parent = [i for i in range(n+1)]
    visited = [0 for _ in range(n+1)]

    ans = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            team_lst = [i]
            dfs(i)
    ans = n - ans
    print(ans)