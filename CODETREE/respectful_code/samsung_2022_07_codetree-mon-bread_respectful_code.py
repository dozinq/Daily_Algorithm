from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

#편의점 위치
combini = []
for _ in range(m):
    combini_x, combini_y = map(int, input().split())
    combini.append([combini_x-1, combini_y-1])

C = deque(combini)
combini.reverse()

# 가장 가까운 베이스캠프 추출
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    distance = [[0]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    temp = []
    while Q:
        x, y = Q.popleft()
        if graph[x][y] == 1:
            temp.append((x, y, distance[x][y]))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] != 9:
                visit[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                Q.append((nx, ny))
    return sorted(temp, key=lambda x:(-x[2], -x[0], -x[1]))

# 현재 위치에서 가장 가까운 편의점으로 이동
def movement(start_x, start_y, des_x, des_y):
    Q = deque()
    Q.append((start_x, start_y))
    visit = [[0]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    visit[start_x][start_y] = 1
    temp = []
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] != 9:
                visit[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if nx == des_x and ny == des_y:
                    graph[nx][ny] = 9
                    return False
                temp.append((nx, ny, abs(des_x-nx)+abs(des_y-ny)))
    return sorted(temp, key=lambda x:(-x[2], -x[0], -x[1]))

time = 0
map_customer = deque()
while True:
    # 편의점에 도착했을 때 제거할 수
    customer_destination = 0
    # 모든 고객이 베이스캠프에 출발하였고, 모든 고객이 편의점에 도착하면 탈출
    if len(C) == 0 and len(map_customer) == 0:
        break

    time += 1
    # 현재 맵의 고객이 있다면 움직임
    for i in range(len(map_customer)):
        m_x, m_y = map_customer.popleft()
        new_location = movement(m_x, m_y, combini[-(i+1)][0], combini[-(i+1)][1])
        if new_location == False:
            customer_destination += 1
            continue
        new_x, new_y, length = new_location.pop()
        map_customer.append((new_x, new_y))
    # 도착한 고객 수만큼 편의점 제거
    for i in range(customer_destination):
        combini.pop()
    # 아직 출발하지 않은 고객이 있다면 베이스 캠프에 추가
    if len(C) > 0:
        now_com = C.popleft()
        c_x, c_y = now_com[0], now_com[1]
        basecamp = bfs(c_x, c_y)
        base_x, base_y, dist = basecamp.pop()
        # 해당 위치 못가게 막기
        graph[base_x][base_y] = 9
        map_customer.append((base_x, base_y))

print(time)