"""
시간 초과를 줄이려면 생각의 전환이 필요하다고 생각한다.
투포인터로 sum을 처리하는 시간마저도 줄여야 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, S = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

ans = float('inf')

start = 0
end = 0
tmp_sum = 0
while end < N:
    tmp_sum += data[end]
    if tmp_sum >= S:
        while tmp_sum >= S:
            tmp_sum -= data[start]
            start += 1
        ans = min(ans, end-start+2)
    end += 1

print(0) if ans == float('inf') else print(ans)