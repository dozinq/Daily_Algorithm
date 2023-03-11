"""
냅색 알고리즘을 사용하여 풀이할 수 있었다.
전에도 비슷한 유형의 문제를 푼 적이 있어서 간단하다고만 생각했는데,
막상 조금만 문제를 꼬아도 냅색 알고리즘이 떠오르지 않았다는 사실에 실망하게 되었다.
기초부터 연습할 필요가 있다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, sys.stdin.readline().split())
wei_lst = list(map(int, sys.stdin.readline().split()))
val_lst = list(map(int, sys.stdin.readline().split()))
# 임의의 wei합이 M보다 크다면, 그 값을 val의 limit값으로 정해놓는다. (val가 limit을 초과 시 무시하기 위한 목적)
val_limit = sum(val_lst)
for i in range(N):
    tmp_sum = sum(wei_lst[0:i+1])
    if tmp_sum >= M:
        val_limit = min(val_limit, sum(val_lst[0:i+1]))
        break

memo = [0] * (val_limit + 1)
for i in range(N):
    wei, val = wei_lst[i], val_lst[i]
    if val < len(memo):
        for i in range(val_limit-val, 0, -1):
            memo[i+val] = max(memo[i+val], memo[i] + wei)
        memo[val] = max(memo[val], wei)

ans = 0
for memo_idx in range(len(memo)):
    if memo[memo_idx] >= M:
        ans = memo_idx
        break

print(ans)
