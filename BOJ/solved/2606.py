"""
양방향 간선을 체크해줬어야 했는데 그걸 미처 체크하지 못하였다.
느려도 좋으니 치밀하게 생각하고 설계하자.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def DFS(num):
    stack = [num]
    global visited
    
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            for i in data[tmp]:
                stack.append(i)
    return

N = int(input())
data_cnt = int(input())

data = [[] for _ in range(N+1)]

for _ in range(data_cnt):
    idx, num = map(int, sys.stdin.readline().split())
    # 이 부분에서 오래 걸림
    if num not in data[idx]:
        data[idx].append(num)
    if idx not in data[num]:
        data[num].append(idx)

visited = []
DFS(1)
print(len(visited) - 1)