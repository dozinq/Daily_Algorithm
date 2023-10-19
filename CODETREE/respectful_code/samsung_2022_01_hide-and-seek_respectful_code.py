n, m, h, k = map(int, input().split())

# 움직이는 방향 표기
runner_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
player_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 보드 생성
# 도망자만 기록할 거임.
board = [[0] * n for _ in range(n)]
# 나무만 기록할 거임.
trees = [[0] * n for _ in range(n)]

# 도망자 입력
runner = {}
for runner_idx in range(1, m + 1):
    tmp = list(map(int, input().split()))
    # 방향은 1 -> 좌우(우방향 우선), 2 -> 상하(하방향 우선)
    # 2를 곱해서 directions에서 각각 0과 2를 받을 수 있도록 함.
    runner[runner_idx] = (tmp[0] - 1, tmp[1] - 1, (tmp[2] - 1) * 2)
    # 보드에 표기
    board[tmp[0] - 1][tmp[1] - 1] = runner_idx

# 나무 입력. 나무는 1로 고정해두기
for tree_idx in range(h):
    loc = list(map(int, input().split()))
    # 나무 보드에 표기. 플레이어들과 겹칠 수 있기 때문
    trees[loc[0] - 1][loc[1] - 1] = 1

# 술래 정보 생성. -2로 표기하며 바라보는 방향을 지정해야함.
# 달팽이 이동을 위한 이동한 거리, 방향당 최대 이동 가능 거리 정보도 가지고 간다.
# 역주행 상황인지도 기록
player = (n // 2, n // 2, 0, 0, 1, False)
board[n // 2][n // 2] = -2

def move_runner(runner_idx):
    now_c, now_r, now_dir = runner[runner_idx]
    next_c = now_c + runner_directions[now_dir][0]
    next_r = now_r + runner_directions[now_dir][1]
    # 격자를 벗어나지 않는 경우
    if 0 <= next_c < n and 0 <= next_r < n:
        # 움직이려는 칸에 술래가 있는가?
        if player[0] == next_c and player[1] == next_r:
            # 그렇다면 움직이지 않는다.
            return
        # 술래가 없다면 움직인다
        else:
            runner[runner_idx] = (next_c, next_r, now_dir)
            return
    # 격자를 벗어나는 경우
    else:
        # 방향을 반대로 틀어준다.
        # 짝수면 + 1, 홀수면 -1
        if now_dir % 2 == 0:
            next_dir = now_dir + 1
        else:
            next_dir = now_dir - 1
        # 새로운 방향에 따른 새로운 다음 위치 갱신
        next_c = now_c + runner_directions[next_dir][0]
        next_r = now_r + runner_directions[next_dir][1]
        # 이 상태에서 술래 존재 유무 파악
        if player[0] == next_c and player[1] == next_r:
            # 그렇다면 움직이지 않는다.
            return
        # 술래가 없다면 움직인다
        else:
            runner[runner_idx] = (next_c, next_r, next_dir)
            return



answer = 0
def move_player():
    global player
    # 술래의 달팽이 이동 진행
    # 전역변수 가야하는 거리를 기준으로 player_directions 상으로
    # 0, 1일 경우 1에서 시작해서 -> 넘어가는 순간 + 1 해주고 -> 2, 3일 경우 2로 지정한 후 -> 또 0, 1로 넘어가는 순간 + 1 해 줌.
    now_c, now_r, now_dir, now_dist, max_dist, isReversed = player
    # 일단 한 번 이동했을 때 max_dist를 넘지 않는다면
    now_dist += 1
    # 일단 가려던 데로 이동하는 건 같음.
    next_c = now_c + player_directions[now_dir][0]
    next_r = now_r + player_directions[now_dir][1]
    # 역방향이 아니라면
    if not isReversed:
        if now_dist < max_dist:
            # 방향은 유지한 채로 가려던 데로 가면 됨.
            player = (next_c, next_r, now_dir, now_dist, max_dist, isReversed)
        # 방향 전환해야할 때가 되었다면
        else:
            # 방향 전환을 해주는 데 4를 넘기면 안되니까
            next_dir = (now_dir + 1) % 4
            # 방향 전환을 했는데 0 또는 2를 만났다면 최대 이동 거리를 늘려줘야 함.
            if next_dir == 0 or next_dir == 2:
                # 단, 늘릴 때 n을 넘기지 않음에 주의
                if max_dist + 1 < n:
                    max_dist += 1
                else:
                    max_dist = n
            # 현재 방향에서 이동거리를 초기화 해주고
            now_dist = 0
            player = (next_c, next_r, next_dir, now_dist, max_dist, isReversed)
    # 역방향으로 가는 중이었다면
    else:
        if now_dist < max_dist:
            # 방향은 유지한 채로 가려던 데로 가면 됨.
            player = (next_c, next_r, now_dir, now_dist, max_dist, isReversed)
        # 방향 전환해야할 때가 되었다면
        else:
            # 방향 전환을 해주는 데 4를 넘기면 안되니까
            next_dir = (now_dir - 1) % 4
            # 방향 전환을 했는데 1 또는 3를 만났다면 최대 이동 거리를 줄여줘야 함.
            if next_dir == 1 or next_dir == 3:
                # 단, 줄일 때 1보다 작아지지 않음에 주의
                if max_dist - 1 > 1:
                    max_dist -= 1
                else:
                    max_dist = 1
            # 현재 방향에서 이동거리를 초기화 해주고
            now_dist = 0
            player = (next_c, next_r, next_dir, now_dist, max_dist, isReversed)
    # 역방향을 해야하는 지 파악해야함.
    # 다음 행선지가 (0, 0) 혹은 (n//2, n//2)라면
    if next_c == 0 and next_r == 0 and not isReversed:
        # 역방향 걸어주고
        # 가려던 방향과 최대 이동 가능 거리 고정
        # [중요] 되돌아갈 때는 예외로 n만큼 가야하고 최초 방향 전환 시 -1을 해주면 안됨.
        # 이를 효과적으로 해결하기 위해 max_dist를 n + 1만큼 주되 now_dist를 1로 준다.
        player = (0, 0, 2, 1, n, True)
    elif next_c == n // 2 and next_r == n // 2 and isReversed:
        player = (n // 2, n // 2, 0, 0, 1, False)


# 보드를 생성해두긴 했지만 사용하는 것은 일단 보류
# 같은 칸에 도망자가 2이상 위치할 수 있지만 이를 보드 상 처리하는 게 비효율적이기 때문
rounds = 0
while rounds < k:
    # 이동해야하는 도망자 이동 진행
    for runner_idx in range(1, m + 1):
        # 생존했다면
        if runner_idx in runner:
            # 해당 도망자가 술래와의 거리가 3이하인지 확인
            if (abs(runner[runner_idx][0] - player[0]) + abs(runner[runner_idx][1] - player[1])) <= 3:
                move_runner(runner_idx)

    # 술래의 이동
    move_player()
    #print(player)

    # 잡았다!
    gatcha = 0
    # 술래의 시야는 무조건 3칸임
    player_c, player_r, player_dir, _, _, _ = player
    for sight in range(3):
        # 술래가 있는가?
        for runner_idx in range(1, m + 1):
            # 생존했다면
            if runner_idx in runner:
                if runner[runner_idx][0] == player_c and runner[runner_idx][1] == player_r:
                    # 나무가 없는가?
                    if trees[player_c][player_r] == 0:
                        gatcha += 1
                        # 잡혔다면 게임에서 제외
                        runner.pop(runner_idx)
        # 시야 업데이트
        player_c += player_directions[player_dir][0]
        player_r += player_directions[player_dir][1]

    # 정답에 반영
    answer += (rounds + 1) * gatcha

    rounds += 1

print(answer)