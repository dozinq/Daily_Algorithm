"""
항상 섣불리 판단하지 말고, 모든 경우를 계산하여 실수하지 않도록 하자.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, K = map(int, input().split())

data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

cnt = 0
for idx in range(len(data)-1, -1, -1):
    if data[idx] <= K:
        cnt += K // data[idx]
        K %= data[idx]

print(cnt)

"""
-코드 리뷰-
: (range의 함수로, reversed를 사용하면 똑같이 구현할 수 있다.)
또한, 배수가 아닐 수도 있으니 나누어지는지 조건을 확인시켜 주어야한다.
"""