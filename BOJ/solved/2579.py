"""
전형적인 DP문제라고 생각된다.
아직은 좀 익숙하진 않지만, 계속 반복하다보면 단순하다고 생각될 것 같긴 하다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

memo = [0] * N
data = [0] * N
for idx in range(N):
    data[idx] = data[idx] = int(sys.stdin.readline())

for idx in range(N):
    if idx >= 3:
        memo[idx] = max(data[idx] + memo[idx - 2], data[idx] + data[idx - 1] + memo[idx - 3])
    elif idx == 0:
        memo[idx] = data[idx]
    elif idx == 1:
        memo[idx] = max(data[idx - 1] + data[idx], data[idx])
    elif idx == 2:
        memo[idx] = max(data[idx - 2] + data[idx], data[idx - 1] + data[idx])

print(memo[N - 1])

