"""
평소 풀던 문제처럼 관습적인 M, N이 바뀌어져 있어서 많이 당황했다.
가로의 길이, 세로의 길이가 아닌 가로의 개수, 세로의 개수로 해석해서 풀었다.
또한, 오랜만에 DFS를 구현해보니 역시 꾸준히 문제를 풀어보아야겠다고 생각이 들었다.
정말 기본중의 기본인 탐색 방법의 구현은 나로 하여금 생각하게 하지 말자.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def DFS(node):
    stack = [node]
    global visited, cnt

    while stack:
        tmp = stack.pop()
        if visited[tmp[0]][tmp[1]] == 0:
            visited[tmp[0]][tmp[1]] = 1
            for i in range(4):
                if 0 <= tmp[0]+dr[i] < M and 0 <= tmp[1]+dc[i] < N:
                    if data[tmp[0]+dr[i]][tmp[1]+dc[i]] == 1:
                        stack.append([tmp[0]+dr[i], tmp[1]+dc[i]])
    cnt += 1
    return

T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    data = list(list(0 for _ in range(N)) for _ in range(M))

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        data[x][y] = 1
    
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = list(list(0 for _ in range(N)) for _ in range(M))
    cnt = 0

    for i in range(M):
        for j in range(N):
            if data[i][j] == 1:
                if visited[i][j] == 0:
                    DFS([i, j])
    
    print(cnt)