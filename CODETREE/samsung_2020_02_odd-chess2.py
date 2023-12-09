import sys
sys.stdin = open('CODETREE/input.txt')

def check_square(x, y):
    return True if 0 <= x < 4 and 0 <= y < 4 else False

def thieves_move():
    for tn in range(1, 17):
        if tn in thieves_data.keys():
            thief = thieves_data[tn]
            thief_arrow = data[thief[0]][thief[1]][1]
            for d in range(8):
                next_arrow = thief_arrow + d - 8 if thief_arrow + d > 8 else thief_arrow + d
                nr, nc = thief[0] + delta[next_arrow][0], thief[1] + delta[next_arrow][1]
                if check_square(nr, nc):
                    if player_data[0] != nr or player_data[1] != nc:
                        # 비어있는 칸인 경우
                        if not data[nr][nc] == []:
                            thieves_data[data[nr][nc][0]] = [thief[0], thief[1]]
                        data[nr][nc], data[thief[0]][thief[1]] = data[thief[0]][thief[1]], data[nr][nc]
                        thieves_data[tn] = [nr, nc]
                        data[nr][nc][1] = next_arrow
                        break
    return

def search_thief(s, r, c, a):
    global player_data
    for pa in range(1, 4):
        nr, nc = r + (delta[a][0] * pa), c + (delta[a][1] * pa)
        if check_square(nr, nc):
            if not data[nr][nc] == []:
                tmp_thief = thieves_data.pop(data[nr][nc][0])
                tmp_data, data[nr][nc] = data[nr][nc], []
                player_data = [nr, nc, tmp_data[1]]
                dfs(s + tmp_data[0], nr, nc, tmp_data[1])
                player_data = [r, c, a]
                thieves_data[tmp_data[0]] = tmp_thief
                data[nr][nc] = tmp_data

    return

def dfs(s, r, c, a):
    global ans
    ans = max(ans, s)
    thieves_move()
    search_thief(s, r, c, a)
    return


# data에 입력 값 삼중 리스트 형식으로 저장
data = []
# 도둑들의 위치 정보는 딕셔너리 형식으로 저장
thieves_data = {}
for n in range(4):
    tmp_input = list(map(int, input().split()))
    tmp_data = []
    for m in range(0, 8, 2):
        tmp_data.append([tmp_input[m], tmp_input[m+1]])
        thieves_data[tmp_input[m]] = [n, m//2]
    data.append(tmp_data)

# player의 위치, 방향과 점수 초기 설정 및 초기 도둑 삭제 작업
player_score = data[0][0][0]
player_data = [0, 0, data[0][0][1]]
thieves_data.pop(data[0][0][0])
data[0][0] = []

delta = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}

ans = 0

dfs(player_score, *player_data)

print(ans)