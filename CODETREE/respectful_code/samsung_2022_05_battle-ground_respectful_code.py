"""
자료구조
플레이어 X좌표, Y좌표, 방향, 초기 능력치, 총, 점수 배열
총 격자: 한 칸에 세 개 이상일 수 있을 수도 있음 -> 힙큐
델타: 인덱스 증가 시 오른쪽으로 돌도록

동작
플레이어 이동: 벽일 때 일반 이동 시 반대, 진 후면 오른쪽 90도
일반 이동: 방향대로 한 칸, 벽일 시 반대로, 플레이어일 시 싸움 호출
진 후 이동: 방향대로 한 칸, 벽이거나 플레이어일 시 오른쪽 90도
버리기: 힙큐에 Push
줍기: 힙큐에 Pop
"""
import heapq
import sys
sys.stdin = open('BOJ/input.txt')

N = M = K = 0
guns = [[]]
players = [[0]]
player_info = [[]]

Y = 0
X = 1
D = 2
ABILITY = 3
GUN = 4
SCORE = 5

SUCCESS = -1
FIGHT = 1

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    get_input()
    #print(player_info)
    run_game()
    print_result()


def print_result():
    for i in range(M):
        print(player_info[i][SCORE], end=' ')


def get_input():
    global N, M, K, guns, player_info, players
    N, M, K = map(int, input().split())
    guns = [[[] for _ in range(N)] for _ in range(N)]
    players = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j] > 0:
                heapq.heappush(guns[i][j], -line[j])

    player_info = [[0 for _ in range(6)] for _ in range(M)]
    for i in range(M):
        y, x, d, s = list(map(int, input().split()))
        y -= 1
        x -= 1
        player_info[i][0:4] = [y, x, d, s]
        players[player_info[i][Y]][player_info[i][X]] = i


def run_game():
    for i in range(K):
        #print("round", i + 1)
        run_round()


def run_round():
    dir = ['↑', '→', '↓', '←']
    for i in range(M):
        result = normal_move(i)
        if result != SUCCESS:
            winner, loser = fight(i, result)
            loser_action(loser)
            winner_action(winner)



def fight(a, b):
    #print("fight!")
    a_info = player_info[a][ABILITY] + player_info[a][GUN]
    b_info = player_info[b][ABILITY] + player_info[b][GUN]

    if a_info != b_info:
        winner = max((a, a_info), (b, b_info), key=lambda x: x[1])[0]
        loser = min((a, a_info), (b, b_info), key=lambda x: x[1])[0]
        player_info[winner][SCORE] += abs(a_info - b_info)
    else:
        a_info = player_info[a][ABILITY]
        b_info = player_info[b][ABILITY]
        winner = max((a, a_info), (b, b_info), key=lambda x: x[1])[0]
        loser = min((a, a_info), (b, b_info), key=lambda x: x[1])[0]


    # print("winner:", winner, "loser:", loser)
    return winner, loser


def get_yx(pid):
    y = player_info[pid][Y]
    x = player_info[pid][X]
    return y, x


def winner_action(pid):
    pick_best_gun(pid)
    y, x = get_yx(pid)
    players[y][x] = pid


def loser_action(pid):
    drop(pid)
    y, x = get_yx(pid)
    adj_y, adj_x = 0, 0

    for i in range(4):
        adj_y, adj_x = get_adj_pos(pid)
        if not is_valid(adj_y, adj_x):
            player_info[pid][D] = (player_info[pid][D] + 1) % 4
            continue
        elif players[adj_y][adj_x] != -1:
            player_info[pid][D] = (player_info[pid][D] + 1) % 4
            continue
        else:
            break

    players[y][x] = -1
    player_info[pid][Y] = adj_y
    player_info[pid][X] = adj_x
    players[adj_y][adj_x] = pid
    pick(pid)


def get_adj_pos(pid):
    now_y, now_x = player_info[pid][Y], player_info[pid][X]
    dy, dx = deltas[player_info[pid][D]]
    adj_y, adj_x = now_y + dy, now_x + dx
    return adj_y, adj_x


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N


def drop(pid):
    if player_info[pid][GUN] > 0:
        y = player_info[pid][Y]
        x = player_info[pid][X]
        heapq.heappush(guns[y][x], -player_info[pid][GUN])
        player_info[pid][GUN] = 0


def pick(pid):
    y = player_info[pid][Y]
    x = player_info[pid][X]

    if len(guns[y][x]) > 0:
        new_gun = heapq.heappop(guns[y][x])
        new_gun *= -1
        #print("pick!", y, x, new_gun)
        player_info[pid][GUN] = new_gun


def pick_best_gun(pid):
    drop(pid)
    pick(pid)



def normal_move(pid):
    adj_y, adj_x = get_adj_pos(pid)
    #print(adj_y, adj_x)

    if not is_valid(adj_y, adj_x):
        player_info[pid][D] = (player_info[pid][D] + 2) % 4

    adj_y, adj_x = get_adj_pos(pid)
    players[player_info[pid][Y]][player_info[pid][X]] = -1

    player_info[pid][Y] = adj_y
    player_info[pid][X] = adj_x

    if players[adj_y][adj_x] != -1:
        return players[adj_y][adj_x]
    else:
        players[adj_y][adj_x] = pid
        pick_best_gun(pid)
        return SUCCESS




solution()