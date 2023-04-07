import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def move_hider():
    for i in range(len(hider)):
        x, y, d = hider[i][0], hider[i][1], hider[i][2]
        if abs(seeker[0] - x) + abs(seeker[1] - y) <= 3:
            # 가려는 위치가 격자 밖이라면,
            if check_square(x+delta[d][0], y + delta[d][1]) == False:
                # 방향 전환하고,
                d = (d + 2) % 4
                # 가려는 위치에 술래가 존재하지 않는 경우에는,
                if seeker[0] != x + delta[d][0] or seeker[1] != y + delta[d][1]:
                    # 이동.
                    x = x + delta[d][0]
                    y = y + delta[d][1]
            # 가려는 위치가 격자 안이라면,
            else:
                # 가려는 위치에 술래가 존재하지 않는 경우에는,
                if seeker[0] != x + delta[d][0] or seeker[1] != y + delta[d][1]:
                    # 이동.
                    x = x + delta[d][0]
                    y = y + delta[d][1]
            # 최종적으로, 위치 및 방향 저장.
            hider[i] = [x, y, d]
    return

def move_seeker():
    global seeker, seeker_dir, seeker_cnt, seeker_reverse
    # 술래는 현재 위치를 방문 표시하고, 자신의 방향대로 이동한다.
    # seeker_cnt의 index. 0:현재 방향, 1: seeker_dir의 참조값, 2: 현재 참조값에서의 count
    seeker[0] += seeker_delta[seeker_cnt[0]][0]
    seeker[1] += seeker_delta[seeker_cnt[0]][1]
    # seeker = [seeker[0] + seeker_delta[seeker_cnt[0]][0]][seeker[1] + seeker_delta[seeker_cnt[0]][1]]
    seeker_cnt[2] += 1
    if seeker_dir[seeker_cnt[1]] == seeker_cnt[2]:
        if seeker_reverse == False:
            seeker_cnt[0] = (seeker_cnt[0] + 1) % 4
            seeker_cnt[1] += 1
            seeker_cnt[2] = 0
        elif seeker_reverse == True:
            seeker_cnt[0] -= 1
            if seeker_cnt[0] == -1:
                seeker_cnt[0] = 3
            seeker_cnt[1] -= 1
            seeker_cnt[2] = 0
    # 먼저, 시작점 혹은 종점에 위치하였는지 판단하고 방향을 바꾼다.
    if seeker[0] == 0 and seeker[1] == 0:
        seeker_reverse = True
        seeker_cnt = [2, len(seeker_dir)-1, 0]
    elif seeker[0] == (n-1) // 2 and seeker[1] == (n-1) // 2:
        seeker_reverse = False
        seeker_cnt = [0, 0, 0]
    catch_hider()
    return

def catch_hider():
    global ans, hider
    tmp_lst = [[seeker[0], seeker[1]], [seeker[0]+seeker_delta[seeker_cnt[0]][0], seeker[1]+seeker_delta[seeker_cnt[0]][1]]]
    if check_square(seeker[0]+2*(seeker_delta[seeker_cnt[0]][0]), seeker[1]+2*(seeker_delta[seeker_cnt[0]][1])) == True:
        tmp_lst.append([seeker[0]+2*(seeker_delta[seeker_cnt[0]][0]), seeker[1]+2*(seeker_delta[seeker_cnt[0]][1])])
    tmp_cnt = 0
    for i in range(len(tmp_lst)):
        if data[tmp_lst[i][0]][tmp_lst[i][1]] == 0:
            for j in range(len(hider)):
                if catched_hider_lst[j] == 0:
                    if hider[j][0] == tmp_lst[i][0] and hider[j][1] == tmp_lst[i][1]:
                        tmp_cnt += 1
                        catched_hider_lst[j] = 1
    if tmp_cnt > 0:
        ans += tmp_cnt * turn
    return

n, m, h, k = map(int, input().split())

data = [list(0 for _ in range(n)) for _ in range(n)]

hider = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
seeker = [(n-1) // 2, (n-1) // 2]
seeker_delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

tmp_dir_cnt = 0
tmp_max = n*n
tmp_i = 1
seeker_dir = []
while tmp_max > 0:
    seeker_dir.append(tmp_i)
    tmp_max -= tmp_i
    tmp_dir_cnt += 1
    if tmp_dir_cnt == 2:
        tmp_i += 1
        tmp_dir_cnt = 0
seeker_dir[-1] -= 1
# seeker_cnt의 index. 0:현재 방향, 1: seeker_dir의 참조값, 2: 현재 참조값에서의 count
seeker_cnt = [0, 0, 0]
seeker_reverse = False

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

catched_hider_lst = [0 for _ in range(m)]
for _ in range(h):
    tree = list(map(lambda x: int(x)-1, input().split()))
    data[tree[0]][tree[1]] = 1

ans = 0
for turn in range(1, k+1):
    move_hider()
    move_seeker()
print(ans)