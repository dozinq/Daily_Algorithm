import sys
sys.stdin = open('BOJ/input.txt')
from collections import deque

def build_factory(n, m, lst):
    tmp_lst = [deque(0 for _ in range(n)) for _ in range(m)]
    for i in range(len(lst)):
        belt_num = i // (n // m)
        tmp_lst[belt_num][i % (n // m)] = lst[i]
    tmp_cnt_lst = [(n//m)-1] * m
    return tmp_lst, tmp_cnt_lst

def drop_box(w_max):
    tmp_cnt = 0
    for idx in range(len(factory)):
        if factory[idx][0] != 0:
            if factory[idx][0][1] <= w_max:
                tmp_box = factory[idx].popleft()
                tmp_cnt += tmp_box[1]
                now_cnt[idx] -= 1
                factory[idx].append(0)
            else:
                tmp_box = factory[idx].popleft()
                factory[idx].append(0)
                factory[idx][now_cnt[idx]] = tmp_box
    return tmp_cnt

def remove_box(n):
    flag = 0
    for i in range(len(factory)):
        for j in range(now_cnt[i] + 1):
            if factory[i][j] != 0:
                if factory[i][j][0] == n:
                    flag = 1
                    factory[i][j] = 0
                    for k in range(j+1, now_cnt[i]+1):
                        factory[i][k-1], factory[i][k] = factory[i][k], 0
                    now_cnt[i] -= 1
    if flag == 0:
        return -1
    elif flag == 1:
        return n

def check_box(n):
    flag = 0
    for i in range(len(factory)):
        if flag == 0:
            for j in range(now_cnt[i] + 1):
                if factory[i][j] != 0:
                    if factory[i][j][0] == n:
                        flag = 1
                        tmp_ans = i+1
                        for _ in range(0, j):
                            tmp_box = factory[i].popleft()
                            factory[i][now_cnt[i]] = tmp_box
                            factory[i].append(0)
                        break
    if flag == 0:
        return -1
    elif flag == 1:
        return tmp_ans

def remove_belt(n):
    if now_cnt[n-1] == -1:
        return -1
    else:
        for i in range(n, n+len(factory)-1):
            if i >= len(factory):
                i = n-len(factory)
            if now_cnt[i] != -1:
                for j in range(now_cnt[n-1]+1):
                    factory[i][now_cnt[i]+1], factory[n-1][j] = factory[n-1][j], 0
                    now_cnt[i] += 1
                now_cnt[n-1] = -1
                return n

q = int(input())

for _ in range(q):
    work = list(map(int, input().split()))
    work_code = work[0]
    if work_code == 100:
        tmp_lst = work[3:]
        box_lst = []
        for i in range(work[1]):
            box_lst.append([tmp_lst[i], tmp_lst[i+work[1]]])
        # factory는 공장의 현재 현황을, now_cnt는 벨트별 사용중인 칸을 의미한다.
        factory, now_cnt = build_factory(work[1], work[2], box_lst)
        print(factory)
    elif work_code == 200:
        print(drop_box(work[1]))
    elif work_code == 300:
        print(remove_box(work[1]))
    elif work_code == 400:
        print(check_box(work[1]))
    elif work_code == 500:
        print(remove_belt(work[1]))
    else:
        print('ERROR: CANT FOUND WORK CODE')
    
    