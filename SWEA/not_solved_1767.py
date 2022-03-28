# def mexi(lst, row, col, core, num):
#     ans_lst = []
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     num += 1
#     if num == core:
#         cnt = 0
#         for i_index in range(len(lst)):
#             for j_index in range(len(lst)):
#                 if lst[i_index][j_index] > 2:
#                     tmp_flag = 1
#                 elif lst[i_index][j_index] == 2:
#                     cnt += 1
#         if tmp_flag == 0:
#             ans_lst.append(cnt)
#     for i in range(row, len(lst)-1):
#         for j in range(col, len(lst)-1):
#             if lst[i][j] == 1:
#                 a = 0
#                 for n in range(4):
#                     tmp_flag = 0
#                     while 0 <= i + (a * dr[n]) < len(lst) and 0 <= j + (a * dc[n]) < len(lst):
#                         if lst[i + (a * dr[n])][j + (a * dc[n])] == 1:
#                             tmp_flag = 1
#                             break
#                         else:
#                             lst[i + (a * dr[n])][j + (a * dc[n])] += 2
#                             a += 1
#                     if tmp_flag == 0:
#                         mexi(lst, i, j, core, num)
#     return ans_lst
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     core = 0
#     for i in range(1, N-1):
#         for j in range(1, N-1):
#             if data[i][j] == 1:
#                 core += 1
#     print(mexi(data, 1, 1, core, 0))
"""
func1. 코어의 위치와 개수를 반환 (테두리 부분 개수는 제외)
func2. 각 코어별로 우하좌상 반복문 실시하여 리스트 변화시킨다.
func3. 코어의 개수와 각 코어들이 변화시킨 횟수가 같다면, 그 때 카운트를 실시시킨다.

"""
def where_core(lst):
    core = []
    for i in range(1, len(lst)-1):
        for j in range(1, len(lst)-1):
            if lst[i][j] == 1:
                core.append((i, j))
    return core

def mexi(lst, core, n, cnt):
    global many, dr, dc, ans_lst
    for m in range(4):              # 각 코어마다 우하좌상 추가시킨다.
        a = 1
        flag = 0
        cnt += 1
        while 0 <= core[n][0]+a*(dr[m]) < len(lst) and 0 <= core[n][1]+a*(dc[m]) < len(lst):
            if lst[core[n][0]+a*(dr[m])][core[n][1]+a*(dc[m])] >= 1:
                flag = 1
            a += 1
        if flag == 0:               # 한 코어 기준으로 한 방향이 모두 0일때,
            a = 1
            while 0 <= core[n][0]+a*(dr[m]) < len(lst) and 0 <= core[n][1]+a*(dc[m]) < len(lst):
                lst[core[n][0]+a*(dr[m])][core[n][1]+a*(dc[m])] += 2
                a += 1
            if n == many:           # 모든 코어의 방향을 다 지정하였다면,
                tmp_cnt = 0
                for i in range(len(lst)):
                    for j in range(len(lst)):
                        if lst[i][j] == 2:
                            tmp_cnt += 1
                ans_lst.append(tmp_cnt)
            else:
                return mexi(lst, core, n+1, cnt)
    if 4**many == cnt:
        return ans_lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ans_lst = []
    core = where_core(data)
    many = len(core)
    print(mexi(data, core, 0, 0))





