import sys
sys.stdin = open('BOJ/input.txt')

def simulate():
    global ans, cnt

    while cnt < m:
        ans += 1
        move_square()
        # check_conv()
        if ans <= m:
            move_basecamp(ans)
    return

def move_square():
    global cnt
    delta = ((-1, 0), (0, -1), (0, 1), (1, 0))
    for idx in range(1, m+1):
        # 격자 내에 사람이 있다면 list 형식이다.
        if type(people[idx]) == list:
            prev_node = 0
            for d in range(4):
                # 이전에 지나온 경로가 아닐때만 탐색.
                if people_prev[idx] != [people[idx][0] + delta[d][0], people[idx][1] + delta[d][1]]:
                    # 갈 수 있는 길인지 탐색.
                    if data[people[idx][0] + delta[d][0]][people[idx][1] + delta[d][1]] != 2:
                        # 유망한 노드가 검색되지 않았었다면,
                        if prev_node == 0:
                            prev_node = [people[idx][0] + delta[d][0], people[idx][1] + delta[d][1]]
                        else:
                            # 이전의 유망한 노드와 현재 갈 수 있는 길과의 비교를 통해 갱신.
                            next_node = abs(conv[idx][0] - (people[idx][0] + delta[d][0])) + abs(conv[idx][1] - (people[idx][1] + delta[d][1]))
                            if next_node < abs(conv[idx][0] - prev_node[0]) + abs(conv[idx][1] - prev_node[1]):
                                prev_node = [people[idx][0] + delta[d][0], people[idx][1] + delta[d][1]]
            # 이전 위치를 저장한다.
            people_prev[idx] = people[idx]
            # 현재 위치를 저장한다.
            people[idx] = [prev_node[0], prev_node[1]]
            bool_conv = check_conv(idx)
            if bool_conv == True:
                data[people[idx][0]][people[idx][1]] = 2
                people[idx] = 0
                cnt += 1
    return

def check_conv(n):
    if people[n][0] == conv[n][0] and people[n][1] == conv[n][1]:
        return True
    return False

def move_basecamp(t):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 비어 있는 베이스 캠프(1)을 탐색한다.
            if data[i][j] == 1:
                # 이전의 위치가 정해져 있었다면, 비교하여 최소인 값으로 갱신한다.
                if type(people[t]) == list:
                    if abs(people[t][0] - conv[t][0]) + abs(people[t][1] - conv[t][1]) > abs(conv[t][0] - i) + abs(conv[t][1] - j):
                        people[t] = [i, j]
                # 이전의 위치가 없다면, 갱신한다.
                else:
                    people[t] = [i, j]
    # 최적 경로의 베이스 캠프에 배정했다면, 그 위치를 들어선 베이스 캠프라는 뜻으로 (2)로 저장한다.
    data[people[t][0]][people[t][1]] = 2
    return


n, m = map(int, input().split())

# data는 현재 격자의 상황을 의미한다. 0은 비어있는 상태, 1은 들어서지 않은 베이스 캠프의 위치, 2는 사람이 있었던 베이스 캠프의 위치 또는 편의점의 위치이다.
data = [list(1 for _ in range(n+2))]
for _ in range(n):
    data.append([1] + list(map(int, input().split())) + [1])
data.append(list(1 for _ in range(n+2)))

# conv는 목표 편의점의 위치를 파악할 수 있다.
conv = [0]
for _ in range(m):
    conv.append(list(map(int, input().split())))

# people은 사람들의 격자 내 현재 위치를 파악할 수 있도록 한다.
people = [0] * (m+1)
# people_prev는 사람들이 바로 직전에 위치했던 곳이다. 이를 통해, 지나온 경로를 채택하지 않을 수 있다.
people_prev = [0] * (m+1)

ans = 0
cnt = 0
simulate()
print(ans)