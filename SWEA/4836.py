# 단점 : 가독성이 매우 떨어짐

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    paper_lst = [[0 for _ in range(10)] for _ in range(10)]         # paper_lst라는 도화지 배열을 생성!
    N = int(input())
    cover_color_lst = []                                            # 색칠되는 색상을 담을 리스트 생성!
    for num in range(N):
        color_lst = list(map(int, input().split()))
        for i in range(color_lst[0], color_lst[2]+1):               # 입력받은 각 케이스들 마다 2번째 인덱스 - 0번째 인덱스 = row
            for j in range(color_lst[1], color_lst[3]+1):           # 입력받은 각 케이스들 마다 4번째 인덱스 - 1번째 인덱스 = col
                paper_lst[i][j] += color_lst[4]                     # 해당 (row, col)에 해당 색상을 색칠하듯, 수를 더해준다.
        cover_color_lst.append(color_lst[4])                        # 한 케이스가 수행되고 나면 칠했던 색상을 색상 리스트에 추가한다.
    ans_color = sum(set(cover_color_lst))                           # 모두 수행되었을 때, 반복되는 색상을 제거(set)해준 후에 색상들의 합을 구하여 변수에 저장한다.

    ans = 0
    for i in range(len(paper_lst)):
        for j in range(len(paper_lst)):
            if paper_lst[i][j] == ans_color:                        # 조건반복문을 통해 겹치는 색상이 도화지에 얼마나 있나 세어준다.
                ans += 1
    print(f'#{tc} {ans}')