import sys
sys.stdin = open('input.txt')

def ans(me):
    stack = [me]
    while stack:
        me = stack.pop()
        if 99 in graph[me]:
            return 1
        else:
            for i in graph[me]:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    tmp_lst = list(map(int, input().split()))

    graph = [[] for _ in range(100)]
    for i in range(E):
        graph[tmp_lst[2*i]].append(tmp_lst[2*i+1])
    visited = []
    print(f'#{tc} {ans(0)}')