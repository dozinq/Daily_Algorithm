from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    
    def check_square(x, y):
        if 0 <= x < n and 0 <= y < m:
            return True
        return False
    
    def bfs(depth):
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r+d[0], c+d[1]
                if nr == 0 and nc == 0:
                    visited[nr][nc] = depth + 1
                    return 1
                else:
                    if check_square(nr, nc):
                        if maps[nr][nc]:
                            if visited[nr][nc] > depth + 1:
                                visited[nr][nc] = depth + 1
                                queue.append((nr, nc))
        if len(queue) > 0:
            return bfs(depth+1)
        else:
            return 0
    
    visited = [list(n*m for _ in range(m)) for _ in range(n)]
    visited[n-1][m-1] = 1
    queue = deque()
    queue.append((n-1, m-1))
    
    # stack = [(0, 0)]
    # depth = 0
    # while stack:
    #     r, c = stack.pop()
    #     for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    #         nr, nc = r + d[0], c + d[1]
    #         if check_square(nr, nc):
    #             if maps[nr][nc]:
    #                 if visited[r][c] + 1 < visited[nr][nc]:
    #                     visited[nr][nc] = visited[r][c] + 1
    #                     stack.append((nr, nc))
                        
    # answer = -1 if visited[n-1][m-1] == n*m else visited[n-1][m-1]
    flag = bfs(1)
    answer = -1 if flag == 0 else visited[0][0]
    return answer