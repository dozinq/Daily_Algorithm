"""
sort의 연속 사용으로 인한 시간초과
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

data = [list(0 for _ in range(2))]

for _ in range(N):
    tmp = sys.stdin.readline().strip()
    if len(tmp) >= M:
        # flag는 찾았는지에 대한 여부이며, 이에 따라 추가하는 방식이 달라진다.
        flag = 0
        for i in range(len(data)):
            if data[i][0] == tmp:
                data[i][1] += 1
                flag = 1
                break
        if flag == 0:
            data.append([tmp, 1])

# 첫 index는 에러 방지용으로 넣어줬던 [0, 0] 이므로 이를 pop한다.
data.pop(0)

# 세번째 조건
data.sort(key=lambda x: x[0])
# 두번째 조건
data.sort(key=lambda x: len(x[0]), reverse=True)
# 첫번째 조건
data.sort(key=lambda x: x[1], reverse=True)

for i in range(len(data)):
    print(data[i][0])

