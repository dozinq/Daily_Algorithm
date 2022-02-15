# N*N 행렬을 모두 0인 원소로 생성한다.
# 델타검색을 통해 '우, 하, 좌, 상'으로 반복할 수 있도록 해주되,
# 0인 값을 만나거나, 인덱스에서 벗어나지 않는다면 델타값은 변함없이 이어지도록 한다.
# 또한 반복문 안에서 1씩 증가하는 num을 설정해주어 입력할 수 있게 한다.

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_lst = [[0 for _ in range(N)] for _ in range(N)]      # 0으로 이루어진 N*N 배열 생성
    dr = [0, 1, 0, -1]                                      # 델타 검색 배열 생성
    dc = [1, 0, -1, 0]

    row = 0
    col = 0
    arrow = 0
    my_lst[0][0] = 1                                        # (0,0)요소는 1로 고정
    for num in range(2, (N**2)+1):                          # 2부터 N*N 까지의 수 배정시킬 계획
        if row + dr[arrow] >= N or col + dc[arrow] >= N:    # 갈 방향이 배열을 넘어간다면,
            arrow += 1                                      # 방향변수를 다음 방향으로!
        elif my_lst[row + dr[arrow]][col + dc[arrow]] != 0: # 0이 아닌 수를 만나면, 즉,
            arrow += 1                                      # 수가 이미 배정되어 있다면 다음 방향!
        if arrow == 4:                                      # 방향변수의 반복을 위한 조건문!
            arrow = 0
        my_lst[row+dr[arrow]][col+dc[arrow]] = num          # 모든 조건을 통과하면 다음 방향에 수 배정
        row += dr[arrow]                                    # 현재 위치를 변수에 저장
        col += dc[arrow]

    print(f'#{tc}')
    for i in my_lst:
        for j in i:
            print(j, end=' ')
        print()