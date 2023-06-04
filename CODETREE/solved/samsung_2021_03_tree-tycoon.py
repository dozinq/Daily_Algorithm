import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def posit_square(num):
    if num < 0:
        return n + num
    elif num >= n:
        return num - n
    else:
        return num

def move_nutri():
    # 1. nutri 들을 d와 p를 참고하여 이동시킨다.
    for i in range(len(nutri)):
        nr = posit_square(nutri[i][0] + (delta[d][0] * p))
        nc = posit_square(nutri[i][1] + (delta[d][1] * p))
        nutri[i] = (nr, nc)
    return

def plus_nutri():
    # 2. 전체 영양제의 위치에 1씩 증가
    for i in range(len(nutri)):
        arr[nutri[i][0]][nutri[i][1]] += 1
    # 3. 전체 영양제 위치마다 대각선 검사 후 cnt만큼 증가
    for i in range(len(nutri)):
        tmp_cnt = 0
        for arrow in range(2, 9, 2):
            nr, nc = nutri[i][0] + delta[arrow][0], nutri[i][1] + delta[arrow][1]
            if check_square(nr, nc) == True:
                if arr[nr][nc] > 0:
                    tmp_cnt += 1
        arr[nutri[i][0]][nutri[i][1]] += tmp_cnt
    return

def reset_nutri():
    global nutri
    # 4. arr를 전체 탐색 후 2씩 감소 및 nutri 배열 초기화 후 append
    new_nutri = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2:
                if (i, j) not in nutri:
                    arr[i][j] -= 2
                    new_nutri.append((i, j))
    nutri = new_nutri
    return

def solve_ans():
    global ans
    for i in range(n):
        for j in range(n):
            ans += arr[i][j]
    return

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# nutri: 초기 영양제 리스트, delta: 방향별 이동 정도
nutri = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]
delta = {1: (0, 1), 2: (-1, 1), 3: (-1, 0), 4: (-1, -1),
        5: (0, -1), 6: (1, -1), 7: (1, 0), 8: (1, 1)}

for _ in range(m):
    d, p = map(int, input().split())
    move_nutri()
    plus_nutri()
    reset_nutri()

ans = 0
solve_ans()
print(ans)