import sys
sys.stdin = open('BOJ/input.txt')

n, m, k = map(int, input().split())

# players의 위치 정보를 수정하지 않을 수 있는 효과와 함께,
# 원소의 값이 float('inf')라면 격자의 범위를 벗어났다고 판단할 수 있게 된다.
data = []
for r in range(n+2):
    if r == 0 or r == n+1:
        data.append(list(float('inf') for _ in range(n+2)))
    else:
        data.append([float('inf')] + list(map(int, input().split())) + [float('inf')])

# players는 [x, y, 방향, 능력치, 총, 포인트] 으로 구성된다.
players = [list(map(int, input().split())) + ([0] * 2) for _ in range(m)]

# 방향은 상우하좌로, 오른쪽으로 90도 전환이 가능하다.
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


for _ in range(k):
    for player in players:
        # 1. 이동
        if data[player[0] + delta[player[2]][0]][player[1] + delta[player[2]][1]] == float('inf'):
            player[2] = (player[2] + 2) % 4    
        player[0] = player[0] + delta[player[2]][0]
        player[1] = player[1] + delta[player[2]][1]
        
        # (플레이어가 있는지 확인. flag는 식별하는 용도.)
        flag = 0
        for enemy in players:
            if enemy != player:
                if enemy[0] == player[0] and enemy[1] == player[1]:
                    flag = 1
                    break
        
        # 2. 플레이어가 없다면 -> 총이 있는지 확인 후, 비교 후 높은 총을 소지 및 드롭
        if flag == 0:
            # 총이 한 자루 있는 경우.
            if type(data[player[0]][player[1]]) == int:
                if data[player[0]][player[1]] > 0:
                    # 그 한 자루가 보유한 총 보다 더 좋을 경우.
                    if data[player[0]][player[1]] > player[4]:
                        data[player[0]][player[1]], player[4] = player[4], data[player[0]][player[1]]
            # 총이 다수일 경우.
            elif type(data[player[0]][player[1]]) == list:
                for gun_idx in range(len(data[player[0]][player[1]])):
                    if data[player[0]][player[1]][gun_idx] > player[4]:
                        data[player[0]][player[1]][gun_idx], player[4] = player[4], data[player[0]][player[1]][gun_idx]
        
        # 3. 플레이어가 있다면 -> 싸움.
        elif flag == 1:
            # player가 이긴 경우 (1)
            if player[3] + player[4] > enemy[3] + enemy[4]:
                # 1. 포인트를 얻음.
                player[5] += (player[3] + player[4]) - (enemy[3] + enemy[4])
                # 2-1. 게임에서 진 enemy는 총을 내려놓고,
                if type(data[enemy[0]][enemy[1]]) == int:
                    data[enemy[0]][enemy[1]] = [data[enemy[0]][enemy[1]], enemy[4]]
                    enemy[4] = 0
                elif type(data[enemy[0]][enemy[1]]) == list:
                    data[enemy[0]][enemy[1]].append(enemy[4])
                    enemy[4] = 0
                # 2-2. 원래 방향대로 이동(다른 플레이어가 존재하거나 격자 밖이라면 오른쪽으로 방향 전환)
                for d in range(4):
                    if data[enemy[0] + delta[(enemy[2] + d) % 4][0]][enemy[1] + delta[(enemy[2] + d) % 4][1]] != float('inf'):
                        search_flag = 0
                        for search_idx in range(m):
                            if players[search_idx] != enemy:
                                if players[search_idx][0] == enemy[0] + delta[(enemy[2] + d) % 4][0] and players[search_idx][1] == enemy[1] + delta[(enemy[2] + d) % 4][1]:
                                    search_flag = 1
                                    break
                        if search_flag == 0:
                            enemy[2] = (enemy[2] + d) % 4
                            enemy[0] = enemy[0] + delta[enemy[2]][0]
                            enemy[1] = enemy[1] + delta[enemy[2]][1]
                            # 총이 한 자루 있는 경우.
                            if type(data[enemy[0]][enemy[1]]) == int:
                                if data[enemy[0]][enemy[1]] > 0:
                                    data[enemy[0]][enemy[1]], enemy[4] = enemy[4], data[enemy[0]][enemy[1]]
                            # 총이 다수일 경우.
                            elif type(data[enemy[0]][enemy[1]]) == list:
                                for gun_idx in range(len(data[enemy[0]][enemy[1]])):
                                    if data[enemy[0]][enemy[1]][gun_idx] > enemy[4]:
                                        data[enemy[0]][enemy[1]][gun_idx], enemy[4] = enemy[4], data[enemy[0]][enemy[1]][gun_idx]
                            break
                # 3. 게임에서 이긴 player는 현재 칸에 위치한 총들 중 가장 좋은 총을 획득한다.
                for gun_idx in range(len(data[player[0]][player[1]])):
                    if data[player[0]][player[1]][gun_idx] > player[4]:
                        data[player[0]][player[1]][gun_idx], player[4] = player[4], data[player[0]][player[1]][gun_idx]
            elif player[3] + player[4] == enemy[3] + enemy[4]:
                # player가 이긴 경우 (2)
                if player[3] > enemy[3]:
                    # 1. 포인트를 얻음.
                    player[5] += (player[3] + player[4]) - (enemy[3] + enemy[4])
                    # 2-1. 게임에서 진 enemy는 총을 내려놓고,
                    if type(data[enemy[0]][enemy[1]]) == int:
                        data[enemy[0]][enemy[1]] = [data[enemy[0]][enemy[1]], enemy[4]]
                        enemy[4] = 0
                    elif type(data[enemy[0]][enemy[1]]) == list:
                        data[enemy[0]][enemy[1]].append(enemy[4])
                        enemy[4] = 0
                    # 2-2. 원래 방향대로 이동(다른 플레이어가 존재하거나 격자 밖이라면 오른쪽으로 방향 전환)
                    for d in range(4):
                        if data[enemy[0] + delta[(enemy[2] + d) % 4][0]][enemy[1] + delta[(enemy[2] + d) % 4][1]] != float('inf'):
                            search_flag = 0
                            for search_idx in range(m):
                                if players[search_idx] != enemy:
                                    if players[search_idx][0] == enemy[0] + delta[(enemy[2] + d) % 4][0] and players[search_idx][1] == enemy[1] + delta[(enemy[2] + d) % 4][1]:
                                        search_flag = 1
                                        break
                            if search_flag == 0:
                                enemy[2] = (enemy[2] + d) % 4
                                enemy[0] = enemy[0] + delta[enemy[2]][0]
                                enemy[1] = enemy[1] + delta[enemy[2]][1]
                                # 총이 한 자루 있는 경우.
                                if type(data[enemy[0]][enemy[1]]) == int:
                                    if data[enemy[0]][enemy[1]] > 0:
                                        data[enemy[0]][enemy[1]], enemy[4] = enemy[4], data[enemy[0]][enemy[1]]
                                # 총이 다수일 경우.
                                elif type(data[enemy[0]][enemy[1]]) == list:
                                    for gun_idx in range(len(data[enemy[0]][enemy[1]])):
                                        if data[enemy[0]][enemy[1]][gun_idx] > enemy[4]:
                                            data[enemy[0]][enemy[1]][gun_idx], enemy[4] = enemy[4], data[enemy[0]][enemy[1]][gun_idx]
                                break
                    # 3. 게임에서 이긴 player는 현재 칸에 위치한 총들 중 가장 좋은 총을 획득한다.
                    for gun_idx in range(len(data[player[0]][player[1]])):
                        if data[player[0]][player[1]][gun_idx] > player[4]:
                            data[player[0]][player[1]][gun_idx], player[4] = player[4], data[player[0]][player[1]][gun_idx]
                # enemy가 이긴 경우 (1)
                elif player[3] < enemy[3]:
                    # 1. 포인트를 얻음.
                    enemy[5] += (enemy[3] + enemy[4]) - (player[3] + player[4])
                    # 2-1. 게임에서 진 player는 총을 내려놓고,
                    if type(data[player[0]][player[1]]) == int:
                        data[player[0]][player[1]] = [data[player[0]][player[1]], player[4]]
                        player[4] = 0
                    elif type(data[player[0]][player[1]]) == list:
                        data[player[0]][player[1]].append(player[4])
                        player[4] = 0
                    # 2-2. 원래 방향대로 이동(다른 플레이어가 존재하거나 격자 밖이라면 오른쪽으로 방향 전환)
                    for d in range(4):
                        if data[player[0] + delta[(player[2] + d) % 4][0]][player[1] + delta[(player[2] + d) % 4][1]] != float('inf'):
                            search_flag = 0
                            for search_idx in range(m):
                                if players[search_idx] != player:
                                    if players[search_idx][0] == player[0] + delta[(player[2] + d) % 4][0] and players[search_idx][1] == player[1] + delta[(player[2] + d) % 4][1]:
                                        search_flag = 1
                                        break
                            if search_flag == 0:
                                player[2] = (player[2] + d) % 4
                                player[0] = player[0] + delta[player[2]][0]
                                player[1] = player[1] + delta[player[2]][1]
                                # 총이 한 자루 있는 경우.
                                if type(data[player[0]][player[1]]) == int:
                                    if data[player[0]][player[1]] > 0:
                                        data[player[0]][player[1]], player[4] = player[4], data[player[0]][player[1]]
                                # 총이 다수일 경우.
                                elif type(data[player[0]][player[1]]) == list:
                                    for gun_idx in range(len(data[player[0]][player[1]])):
                                        if data[player[0]][player[1]][gun_idx] > player[4]:
                                            data[player[0]][player[1]][gun_idx], player[4] = player[4], data[player[0]][player[1]][gun_idx]
                                break
                    # 3. 게임에서 이긴 enemy는 현재 칸에 위치한 총들 중 가장 좋은 총을 획득한다.
                    for gun_idx in range(len(data[enemy[0]][enemy[1]])):
                        if data[enemy[0]][enemy[1]][gun_idx] > enemy[4]:
                            data[enemy[0]][enemy[1]][gun_idx], enemy[4] = enemy[4], data[enemy[0]][enemy[1]][gun_idx]
            # enemy가 이긴 경우 (2)
            else:
                # 1. 포인트를 얻음.
                enemy[5] += (enemy[3] + enemy[4]) - (player[3] + player[4])
                # 2-1. 게임에서 진 player는 총을 내려놓고,
                if type(data[player[0]][player[1]]) == int:
                    data[player[0]][player[1]] = [data[player[0]][player[1]], player[4]]
                    player[4] = 0
                elif type(data[player[0]][player[1]]) == list:
                    data[player[0]][player[1]].append(player[4])
                    player[4] = 0
                # 2-2. 원래 방향대로 이동(다른 플레이어가 존재하거나 격자 밖이라면 오른쪽으로 방향 전환)
                for d in range(4):
                    if data[player[0] + delta[(player[2] + d) % 4][0]][player[1] + delta[(player[2] + d) % 4][1]] != float('inf'):
                        search_flag = 0
                        for search_idx in range(m):
                            if players[search_idx] != player:
                                if players[search_idx][0] == player[0] + delta[(player[2] + d) % 4][0] and players[search_idx][1] == player[1] + delta[(player[2] + d) % 4][1]:
                                    search_flag = 1
                                    break
                        if search_flag == 0:
                            player[2] = (player[2] + d) % 4
                            player[0] = player[0] + delta[player[2]][0]
                            player[1] = player[1] + delta[player[2]][1]
                            # 총이 한 자루 있는 경우.
                            if type(data[player[0]][player[1]]) == int:
                                if data[player[0]][player[1]] > 0:
                                    data[player[0]][player[1]], player[4] = player[4], data[player[0]][player[1]]
                            # 총이 다수일 경우.
                            elif type(data[player[0]][player[1]]) == list:
                                for gun_idx in range(len(data[player[0]][player[1]])):
                                    if data[player[0]][player[1]][gun_idx] > player[4]:
                                        data[player[0]][player[1]][gun_idx], player[4] = player[4], data[player[0]][player[1]][gun_idx]
                            break
                # 3. 게임에서 이긴 enemy는 현재 칸에 위치한 총들 중 가장 좋은 총을 획득한다.
                for gun_idx in range(len(data[enemy[0]][enemy[1]])):
                    if data[enemy[0]][enemy[1]][gun_idx] > enemy[4]:
                        data[enemy[0]][enemy[1]][gun_idx], enemy[4] = enemy[4], data[enemy[0]][enemy[1]][gun_idx]

for elem in players:
    print(elem[5], end=" ")
