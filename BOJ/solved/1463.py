"""
DP에 대한 이해가 부족하다고 판단된다.
정확히는, 재귀 함수의 구현과 마찬가지로, 짧은 코드일 수록 섣불리 판단하기 쉽다는 것이다.
오류가 두 번 정도 났었고, 이는 모두 분기별 대응에 실수를 한 탓이다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

memo = [0] * (N + 1)

for idx in range(2, N + 1):
    memo[idx] = memo[idx - 1] + 1
    if idx % 2 == 0:
        memo[idx] = min(memo[idx // 2] + 1, memo[idx])
    if idx % 3 == 0:
        memo[idx] = min(memo[idx // 3] + 1, memo[idx])

print(memo[N])