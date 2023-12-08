import sys
sys.stdin = open('CODETREE/input.txt')

def put_block(type, row, col):
    for yr in range(2):
        board = yellow_board
        # 각 파라미터 회전 조작 시켜야 함
        if yr == 1:
            board = red_board
            # 회전 공식 점화식 유도 방법 잊어서 규칙 찾아서 세웠음
            row, col = col, (row + 1) % 4 if row % 2 else (row + 3) % 4
            if type == 2:
                type = 3
            elif type == 3:
                type = 2
                # type이 3인 경우는 type 2으로 변환되면서 col값도 1 감소하게 되는 설정이다.
                col -= 1
        if type == 1:
            # flag는 하향 허용 지점을 알려주는 변수
            flag = -1
            for r in range(4):
                if board[r][col] == 0:
                    flag = r
                else:
                    break
            # 내려갈 곳이 없다면 다음과 같이 보드를 조작해야 한다.
            if flag == -1:
                for br in range(3, 0, -1):
                    board[br] = board[br-1]
                board[0] = [0, 0, 0, 0]
                board[0][col] = 1
            else:
                board[flag][col] = 1
                if not board[flag].count(0):
                    clear_block(yr)
        elif type == 2:
            flag = -1
            for r in range(4):
                if board[r][col] == 0 and board[r][col+1] == 0:
                    flag = r
                else:
                    break
            if flag == -1:
                for br in range(3, 0, -1):
                    board[br] = board[br-1]
                board[0] = [0, 0, 0, 0]
                board[0][col], board[0][col+1] = 1, 1
            else:
                board[flag][col], board[flag][col+1] = 1, 1
                if not board[flag].count(0):
                    clear_block(yr)
        elif type == 3:
            # flag = -1
            # for r in range(4):
            #     if board[r][col] == 0:
            #         flag = r
            # # 두 칸 다 막혀있는 경우,
            # if flag == -1:
            #     for br in range(3, 1, -1):
            #         board[br] = board[br-2]
            #     board[0], board[1] = [0, 0, 0, 0], [0, 0, 0, 0]
            #     board[0][col], board[1][col] = 1, 1
            # # 한 칸만 막혀있는 경우,
            # elif flag == 0:
            #     for br in range(3, 0, -1):
            #         board[br] = board[br-1]
            #     board[0] = [0, 0, 0, 0]
            #     board[0][col], board[1][col] = 1, 1
            # else:
            #     board[flag][col], board[flag-1][col] = 1, 1
            for _ in range(2):
                flag = -1
                for r in range(4):
                    if board[r][col] == 0:
                        flag = r
                    else:
                        break
                if flag == -1:
                    for br in range(3, 0, -1):
                        board[br] = board[br-1]
                    board[0] = [0, 0, 0, 0]
                    board[0][col] = 1
                else:
                    board[flag][col] = 1
                    if not board[flag].count(0):
                        clear_block(yr)
    return

def clear_block(yelorred):
    global ans
    board = red_board if yelorred else yellow_board
    for row in range(4):
        if board[row].count(0) == 0:
            ans += 1
            board[row] = [0, 0, 0, 0]
            for br in range(row, 0, -1):
                board[br] = board[br-1]
            board[0] = [0, 0, 0, 0]
    return

yellow_board = [list(0 for _ in range(4)) for _ in range(4)]
red_board = [list(0 for _ in range(4)) for _ in range(4)]
ans = 0

k = int(input())

for _ in range(k):
    # t, x, y 입력
    tmp_input = map(int, input().split())
    put_block(*tmp_input)

print(ans)
ans = 0
for r in range(4):
    for c in range(4):
        if yellow_board[r][c] == 1:
            ans += 1
        if red_board[r][c] == 1:
            ans += 1
print(ans)

    
