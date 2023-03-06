"""
전에 풀었었던 RGB 색깔칠하며 내려가기와 문제 유형이 비슷하였다.
오히려 그것을 풀었을 때보다 조금 수월했던 것 같다고도 느꼈다.
적은 메모리로 제한되어 있어서 데이터를 입력받는 동시에 작업을 수행할 수 있도록 하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

# 한번 시행할때마다 최솟값과 최댓값으로 갱신할 수 있는 저장공간 필요.
memo_max = list(map(int, sys.stdin.readline().split()))
memo_min = memo_max[:]

for _ in range(N-1):
    data = list(map(int, sys.stdin.readline().split()))

    tmp_max = [0, 0, 0]
    tmp_min = [0, 0, 0]
    # 경로는 총 8개. 0-0, 0-1, 1-0, 1-1, 1-2, 2-1, 2-2.
    tmp_max[0] = max((memo_max[0] + data[0]), (memo_max[1] + data[0]))
    tmp_max[1] = max((memo_max[0] + data[1]), (memo_max[1] + data[1]), (memo_max[2] + data[1]))
    tmp_max[2] = max((memo_max[1] + data[2]), (memo_max[2] + data[2]))

    tmp_min[0] = min((memo_min[0] + data[0]), (memo_min[1] + data[0]))
    tmp_min[1] = min((memo_min[0] + data[1]), (memo_min[1] + data[1]), (memo_min[2] + data[1]))
    tmp_min[2] = min((memo_min[1] + data[2]), (memo_min[2] + data[2]))

    memo_max = tmp_max[:]
    memo_min = tmp_min[:]

print(f'{max(memo_max)} {min(memo_min)}')

"""
-코드 리뷰-
: 나와 동일한 방식으로 풀이한 사람들이 많았다.
이는 DP라는 명칭으로 불리운다.
"""