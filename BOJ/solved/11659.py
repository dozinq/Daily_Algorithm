"""
많은 고민을 해보았다.
생각나는대로 구현한다면 당연히 시간초과를 맞을 거라 예상했다.
그러다가 0 <= i <= j <= N 이라는 조건을 보고 j까지의 합 - i까지의 합 이므로
미리 합을 저장해두기로 하였다.
그 후 코드리뷰를 해보니, 다들 이렇게 풀었고, 이러지 않고서는 시간초과라고 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

tmp = map(int, sys.stdin.readline().split())
data = [0] * N

idx = 0
for i in tmp:
    if idx > 0:
        data[idx] = data[idx-1] + i
    elif idx == 0:
        data[idx] = i
    idx += 1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1

    if i == 0:
        ans = data[j]
    else:
        ans = data[j] - data[i - 1]

    # for idx in range(i, j + 1):
    #     ans += data[idx]
    print(ans)