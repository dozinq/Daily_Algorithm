import sys
sys.stdin = open('BOJ/input.txt')

def exception_1(x, y):
    for dlt in range(4):
        if check_square(x+delta[dlt][0], y+delta[dlt][1]) == True:
            if data[x+delta[dlt][0]][y+delta[dlt][1]] == 4:
                return False
    return True

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def move_people():
    global data, score_data
    cnt = 0
    for i in range(n):
        if cnt < m:
            for j in range(n):
                if cnt < m:
                    if data[i][j] == 1:
                        if score_data[i][j] == 0:
                            cnt += 1
                            stack = [(i, j)]
                            flag_3 = 0
                            flag_3_1 = 0
                            score = 1
                            while stack:
                                now_i, now_j = stack.pop()
                                if score_data[now_i][now_j] == 0:
                                    for d in range(4):
                                        next_i, next_j = now_i+delta[d][0], now_j+delta[d][1]
                                        if check_square(next_i, next_j) == True:
                                            if data[next_i][next_j] == 4:
                                                data[next_i][next_j], data[now_i][now_j] = data[now_i][now_j], data[next_i][next_j]
                                                score_data[next_i][next_j] = score
                                                score += 1
                                            elif data[next_i][next_j] == 2:
                                                stack.append((next_i, next_j))
                                            elif data[next_i][next_j] == 3:
                                                if data[now_i][now_j] == 1 and exception_1(now_i, now_j) == True:
                                                    data[next_i][next_j], data[now_i][now_j] = data[now_i][now_j], 4
                                                    score_data[next_i][next_j] = score
                                                    score += 1
                                                    flag_3_1 = (next_i, next_j)
                                                else:
                                                    flag_3 = (next_i, next_j)
                                if flag_3_1 == 0 and flag_3 != 0:
                                    data[now_i][now_j], data[flag_3[0]][flag_3[1]] = data[flag_3[0]][flag_3[1]], data[now_i][now_j]
                                    score_data[now_i][now_j] = score
                                    break
                            if flag_3_1 != 0:
                                for dlt in range(4):
                                    if check_square(flag_3_1[0]+delta[dlt][0], flag_3_1[1]+delta[dlt][1]) == True:
                                        if data[flag_3_1[0]+delta[dlt][0]][flag_3_1[1]+delta[dlt][1]] == 4:
                                            data[flag_3_1[0]+delta[dlt][0]][flag_3_1[1]+delta[dlt][1]] = 3
                                            score_data[flag_3_1[0]+delta[dlt][0]][flag_3_1[1]+delta[dlt][1]] = score
    print(score_data)
    return

def throw_ball(t):
    # t에 따른 방향
    arrow = (t // n) % 4
    # t에 따른 행또는 열의 번호
    if arrow == 0:
        for i in range(n):
            if data[t % n][i] != 0 and data[t % n][i] != 4:
                get_score(t % n, i)
                break
    elif arrow == 1:
        for i in range(n-1, -1, -1):
            if data[i][t % n] != 0 and data[i][t % n] != 4:
                get_score(i, t % n)
                break
    elif arrow == 2:
        for i in range(n-1, -1, -1):
            if data[t % n][i] != 0 and data[t % n][i] != 4:
                get_score(t % n, i)
                break
    elif arrow == 3:
        for i in range(n):
            if data[i][t % n] != 0 and data[i][t % n] != 4:
                get_score(i, t % n)
                break
    return

def get_score(x, y):
    global ans, data
    ans += (score_data[x][y])**2
    team_head = [x, y]
    team_tail = [x, y]
    stack = [(x, y)]
    while stack:
        now_x, now_y = stack.pop()
        for d in range(4):
            next_x, next_y = now_x+delta[d][0], now_y+delta[d][1]
            if check_square(next_x, next_y) == True:
                if score_data[next_x][next_y] > 0:
                    if score_data[next_x][next_y] < score_data[team_head[0]][team_head[1]]:
                        team_head = [next_x, next_y]
                        stack.append((next_x, next_y))
                    if score_data[team_tail[0]][team_tail[1]] < score_data[next_x][next_y]:
                        team_tail = [next_x, next_y]
                        stack.append((next_x, next_y))
    data[team_head[0]][team_head[1]], data[team_tail[0]][team_tail[1]] = data[team_tail[0]][team_tail[1]], data[team_head[0]][team_head[1]]
    return

# n: 격자 크기, m: 팀 개수, k: 라운드 수
n, m, k = map(int, input().split())

# (0: 빈칸, 1: 머리사람, 2: 나머지 인원, 3: 꼬리사람, 4: 이동 선)
data = [list(map(int, input().split())) for _ in range(n)]

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))

ans = 0
for turn in range(k):
    # 점수를 쉽게 계산할 수 있게 하는 점수판
    score_data = [list(0 for _ in range(n)) for _ in range(n)]
    move_people()
    throw_ball(turn)
    
print(ans)