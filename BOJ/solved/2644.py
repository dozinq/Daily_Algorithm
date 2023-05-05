import sys
sys.stdin = open('BOJ/input.txt')

def dfs(node, depth):
    global ans
    if node not in visited:
        visited.append(node)
        if node == end:
            ans = depth
            return
        else:
            for i in range(2):
                for j in data[node][i]:
                    dfs(j, depth+1)
    return

n = int(input())
start, end = map(int, input().split())
m = int(input())

# 각 노드의 0번 인덱스: 부모, 1번 인덱스: 자식
data = [list(list() for _ in range(2)) for _ in range(n+1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    data[tmp[0]][1].append(tmp[1])
    data[tmp[1]][0].append(tmp[0])

ans = -1
visited = []
dfs(start, 0)
print(ans)
