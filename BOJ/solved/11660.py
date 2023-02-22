"""
역시 브루트포스? 형식으로 탐색하였더니 시간초과오류를 만났다.(주석처리로 아래에 작성한 부분)
애초에 저장할 때부터 누적합으로 저장할 수 있도록 한다.
단, 나의 풀이방법에서는 누적합도 정방형 모양으로 잘릴 수 있도록 저장해야 한다.
그러기 위해서는 data[x][y] = data[x-1][y] + data[x][y-1] - data[x-1][y-1] 과 같은 형식으로 저장하는 것이 적합하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

# data의 저장 로직
data = []
for idx in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    # 첫째줄일 때의 저장 방법
    if idx == 0:
        for i in range(len(tmp)-1):
            tmp[i+1] += tmp[i] 
        data.append(tmp)
    # 첫째줄은 아니지만, 0번째 인덱스일 경우는 예외처리로 저장
    else:
        tmp[0] += data[idx-1][0]
        for i in range(1, len(tmp)):
            tmp[i] += tmp[i-1] + data[idx-1][i] - data[idx-1][i-1]
        data.append(tmp)        

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    # ans는 기본적으로 (x2, y2)의 값이 되어야 하므로
    ans = data[x2][y2]
    # x1이 0이 아니어서, 첫째줄부터가 아니라면,
    if x1 != 0:
        ans -= data[x1-1][y2]
    # y1이 0이 아니어서, 왼쪽 전체를 의미하는 것이 아니라면,
    if y1 != 0:
        ans -= data[x2][y1-1]
    # 위의 두 조건을 모두 해당하여 다 빼주었다면, 2번 빼준 부분을 더해준다.
    if x1 != 0 and y1 != 0:
        ans += data[x1-1][y1-1]
    
    print(ans)


# 브루트 포스
# data = []
# for _ in range(N):
#     data.append(list(map(int, sys.stdin.readline().split())))

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     x1 -= 1
#     y1 -= 1
#     x2 -= 1
#     y2 -= 1

#     ans = 0
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             ans += data[i][j]
#     print(ans)
