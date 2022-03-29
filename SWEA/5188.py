"""
느낀 점 -
1. 함수를 보고 이해하는 것과 직접 구현하는 것은 마치, 햄과 햄토리다.
2. ans_lst라는 리스트를 만들어 함수가 실행되면 결과값들이 append 될 수 있게 하였더니 '제한시간을 초과' 하였다.
-> 이를 개선하기 위해, 결과값이 만들어 질 때마다 현재의 최소값과 비교하며 갱신시킬 수 있도록 하였다.
"""

import sys
sys.stdin = open('input.txt')

def sum_data(x, y, dist):                       # 현재 x, y의 위치와 거리누적값인 dist를 인자로 갖는 함수 생성!
    global ans                                  # 최솟값이 변경될 수 있도록 한다.
    if x == N - 1 and y == N - 1:               # 마지막 인덱스라면,
        dist += data[x][y]                      # 마지막 인덱스의 값도 누적시키고,
        if ans == 0:                            # 단, 함수가 처음 시행되었다면,
            ans = dist                          # 그 때에만 dist를 ans값에 넣는다.
        else:                                   # 두번째 시행될 때부터,
            ans = min(ans, dist)                # ans와 현재 dist값을 비교할 수 있도록 한다. 
    else:                                       #
        if x < N - 1:                           # x 인덱스는 행값을, y 인덱스는 열값을 뜻한다.(만들다보니 이렇게 해버림.. 대충 살자)
            sum_data(x+1, y, dist+data[x][y])   # 행 값이 변경될 수 있다면, 변경시킨다.
        if y < N - 1:                           # 위의 함수를 시행한 후에 열 값이 변경될 수 있다면,
            sum_data(x, y+1, dist+data[x][y])   # 열 값을 변경시킨다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # ans_lst = []                              # 이러면 시간이 더 걸린단다~~
    ans = 0
    sum_data(0, 0, 0)
    print(f'#{tc} {ans}')