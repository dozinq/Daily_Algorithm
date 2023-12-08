import sys
sys.stdin = open('CODETREE/input.txt')

def check_blank(put_num, row, col):
    board = yellow_board if put_num == 0 else red_board
    flag = -1
    for r in range(4):
        if not board[r][col]:
            flag = r
    return board, flag

def put_block(type, row, col):
    for put_num in range(2):
        # 두 번째 놓을 때는 red_board에 놓기 위해 parameter를 조작해주어야 한다.
        if put_num == 1:
            pass
        if type == 1:
            board, flag = check_blank(put_num, row, col)
            if flag == -1:
                for br in range(3, 0, -1):
                    board[br] = board[br-1]
                board[0] = [0, 0, 0, 0]
                board[0][col] = 1
            else:
                board[flag][col] = 1
        elif type == 2:
            for plus_col in range(2):
                board, flag = check_blank(put_num, row, col + plus_col)

    return

yellow_board = [list(0 for _ in range(4)) for _ in range(4)]
red_board = [list(0 for _ in range(4)) for _ in range(4)]
ans = 0

k = int(input())
for _ in range(k):
    put_block(*map(int, input().split()))

    

