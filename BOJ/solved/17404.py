"""
많이 생각해보고 그려보기도 하였는데 도무지 감이 안잡히다가, 막상 코드를 짜보니
시작점을 다르게 표시하고 찾으면 될 것 같아서 그렇게 표시하였다.
또한, 코드 리뷰를 해보니 애초에 dp에 INF들로 초기화 시킨다면 더 깔끔한 코드를 만들 수 있다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
ans = float('inf')

# 0번, 1번, 2번 인덱스 총 3번을 진행해야 하므로.
for i in range(3):
    # 진행할때 마다 해당하지 않는 곳은 무한대 처리를 해줄 것이며, 마지막에 되돌려 놓기 위해 tmp 변수에 미리 담아둔다.
    tmp_1 = data[0][(i+1)%3]
    tmp_2 = data[0][(i+2)%3]
    data[0][(i+1)%3] = float('inf')
    data[0][(i+2)%3] = float('inf')
    # memo를 데이터의 0번째 행으로 초기화해주고, 다음의 루트를 진행한다.
    memo = data[0][:]
    tmp_lst = [0, 0, 0]
    for n in range(N-1):
        tmp_lst[0] = min(memo[1] + data[n+1][0], memo[2] + data[n+1][0])
        tmp_lst[1] = min(memo[0] + data[n+1][1], memo[2] + data[n+1][1])
        tmp_lst[2] = min(memo[0] + data[n+1][2], memo[1] + data[n+1][2])
        memo = tmp_lst[:]
    # ans값에 저장하기 위해 다음의 작업을 수행한다.
    memo[i] = float('inf')
    ans = min(ans, memo[0], memo[1], memo[2])
    # 다시 원래대로 데이터를 돌려놓는다.
    data[0][(i+1)%3] = tmp_1
    data[0][(i+2)%3] = tmp_2

print(ans)