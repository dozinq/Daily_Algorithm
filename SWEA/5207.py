"""
느낀 점 -
1. 문제를 이해하는 데 시간이 걸렸다. (반복하는데 왜 m이 찾는 숫자이면 방향을 무시하는 건지.. 많은 시행착오 끝에 풀었다.)
2. 이진 탐색은 간단하다. 다만, 이 문제는 이진 탐색에 다른 귀찮은 개념을 더해서 복잡해졌던 것이다.
"""

import sys
sys.stdin = open('input.txt')

def binary(n):
    l = 0                       # l, r, m 은 모두 '인덱스위치'를 표현하는 변수!
    r = N-1
    tmp_ans = 0
    while l <= r:
        m = (l + r) // 2        # 반복문이 시행될 때 마다 m은 l과 r을 더하여 2로 나눈 몫으로 갱신!
        if n == A[m]:           # n이 m위치에 존재한다면,
            tmp_ans = 0         # tmp_ans 값을 0으로 변환하고 탈출한다.
            break               # 어차피 여기까지 왔다면 tmp_ans는 0, 1, -1 셋 중 하나일 것이므로 문제 조건에 맞는다.
        if n < A[m]:            # n이 m위치보다 왼쪽에 있다면,
            r = m-1             # r 위치를 변동시키고,
            if tmp_ans == 1:    # 만약 이전 반복상황에서도 방금 이 상황이었다면,
                break           # 문제조건에 맞지 않으므로 tmp_ans는 그대로 냅두고 탈출만 시킨다.
            else:               # 현재 m이 0이든 -1이든 문제상황에는 적합하므로,
                tmp_ans = 1     # tmp_ans는 1로 변경시킨다.
        elif n > A[m]:          # n이 m위치보다 오른쪽에 있다면,
            l = m+1             # l 위치를 변동시키고,
            if tmp_ans == -1:   # 만약 이전 반복상황에서도 방금 이 상황이었다면,
                break           # 문제조건에 맞지 않으므로 tmp_ans는 그대로 냅두고 탈출만 시킨다.
            else:               # 현재 m이 0이든 1이든 문제상황에는 적합하므로,
                tmp_ans = -1    # tmp_ans는 -1로 변경시킨다.
    if tmp_ans == 0:            # tmp_ans가 최종적으로 0이라면,
        return 1                # 문제 상황에 적합하므로 1을 반환한다.
    return 0                    # 아니라면, 0 반환!

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        if B[i] in A:
            ans += binary(B[i])     # ans 값에는 몇 가지의 정답경우가 있는지를 누적시킨다.
    print(f'#{tc} {ans}')