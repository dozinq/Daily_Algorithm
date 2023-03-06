"""
모든 다각형은 삼각형의 넓이의 합이라고 생각할 수 있었으나,
그려볼때에 각도가 다양한 다각형의 넓이를 어떻게 구할 지 의문이었고, 다각형의 넓이를 구하는 방법을 찾아보았다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.append(data[0])

ans = 0
for idx in range(N):
    first = data[idx][0] * data[idx+1][1]
    second = data[idx][1] * data[idx+1][0]
    ans += first - second

print(abs(ans)/2)


