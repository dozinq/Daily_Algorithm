import sys
sys.stdin = open('input.txt')

N, M, V = map(int, input().split())
data = [[] for _ in range(N+1)]
d_visited = [V]
d_stack = [V]
b_visited = [V]
b_queue = [V]

def dfs():
    node = d_stack.pop()
    for i in data[node]:
        if i not in d_visited:
            d_visited.append(i)
            d_stack.append(i)
            dfs()
    return

def bfs():
    if len(b_queue) == 0:
        return
    node = b_queue.pop(0)
    for i in data[node]:
        if i not in b_visited:
            b_queue.append(i)
            b_visited.append(i)
    bfs()

for _ in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

# print(data)
for i in range(len(data)):
    data[i].sort()
#
# print(data)

dfs()
bfs()
for idx in d_visited:
    print(idx, end=' ')
print()

for idx in b_visited:
    print(idx, end=' ')

# print(d_visited)
# print(b_visited)