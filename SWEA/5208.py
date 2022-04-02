"""
느낀 점 -
1. 제한시간 초과 에러를 마주치지 않으려고, 나름대로 최대한 시간을 단축하려 해봤다.
-> 탐색 범위를 최대로 늘려주었다.(예를 들어, 1씩 조금씩 가는 것은 방법이 아닌데도 먼저 시도하게 될 테니 말이다.)
"""

import sys
sys.stdin = open('input.txt')

def bus(num, cnt):
    global ans

    if cnt > ans:
        return

    if num >= N:
        ans = min(ans, cnt)
        return

    for n in range(num+data[num], num, -1):         # 범위를 range(num+1, num+data[num]+1) 로 해준다면 제한시간 초과 에러를 마주치더라.
        if num == 1:
            bus(n, cnt)
        bus(n, cnt+1)


T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    ans = N
    visited = [0] * N
    bus(1, 0)
    print(f'#{tc} {ans}')