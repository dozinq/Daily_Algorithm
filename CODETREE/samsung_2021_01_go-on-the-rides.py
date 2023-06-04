import sys
sys.stdin = open('BOJ/input.txt')

def check_square(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def seat_student():
    # 순서대로, 어떤 자리가 가장 적합한지를 탐색한 후 앉히는 함수이다.
    for stu in seq_lst:
        # tmp_seat => 0: 행, 1: 열, 2: 인접 선호 학생 수, 3: 인접한 칸 중 빈 칸의 수
        tmp_seat = (0, 0, 0, 0)
        for r in range(n):
            for c in range(n):
                # 0. 현재 (r, c)가 빈 칸인지
                if arr[r][c] == 0:
                    if tmp_seat == (0, 0, 0, 0):
                        tmp_seat = (r, c, search_like(stu, r, c), search_empty(r, c))
                    # 1. 인접한 곳에 좋아하는 학생이 있는지
                    like_sum = search_like(stu, r, c)
                    # 1-1. 같은 경우는 continue X
                    if tmp_seat[2] == like_sum:
                        # 2. 인접한 곳에 비어있는 칸이 몇 개인지
                        empty_sum = search_empty(r, c)
                        if tmp_seat[3] < empty_sum:
                            tmp_seat = (r, c, like_sum, empty_sum)
                        else:
                            continue
                    elif tmp_seat[2] < like_sum:
                        tmp_seat = (r, c, like_sum, search_empty(r, c))
                        continue
                    elif tmp_seat[2] > like_sum:
                        continue
        arr[tmp_seat[0]][tmp_seat[1]] = stu
    return

def search_like(s, x, y):
    tmp_sum = 0
    for d in delta:
        new_r, new_c = x + d[0], y + d[1]
        if check_square(new_r, new_c) == True:
            if arr[new_r][new_c] in stu_lst[s]:
                tmp_sum += 1
    return tmp_sum

def search_empty(x, y):
    tmp_sum = 0
    for d in delta:
        new_r, new_c = x + d[0], y + d[1]
        if check_square(new_r, new_c) == True:
            if arr[new_r][new_c] == 0:
                tmp_sum += 1
    return tmp_sum

def calc_score():
    global ans
    for r in range(n):
        for c in range(n):
            tmp_cnt = 0
            for d in delta:
                new_r, new_c = r+d[0], c+d[1]
                if check_square(new_r, new_c) == True:
                    if arr[new_r][new_c] in stu_lst[arr[r][c]]:
                        tmp_cnt += 1
            if tmp_cnt > 0:
                ans += 10 ** (tmp_cnt-1)
    return

# n: 격자 크기, arr: 격자, stu_lst: 좋아하는 학생들의 번호(인덱스로 저장), seq_lst: 탑승 순서를 저장
n = int(input())
arr = list(list(0 for _ in range(n)) for _ in range(n))
stu_lst = [0] + list(list() for _ in range(n*n))
seq_lst = []

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(n*n):
    tmp = tuple(map(int, input().split()))
    stu_lst[tmp[0]] = tmp[1:5]
    seq_lst.append(tmp[0])

ans = 0
seat_student()
calc_score()
print(ans)

