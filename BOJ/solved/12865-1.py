"""
이전의 탐색 구현에서 시간초과가 자꾸 발생하여 다른 해결 방식을 생각해 보았다.
메모이제이션을 이용하여 입력되는 값마다 W-K의 범위 안에 있는 최대값과 비교하여 재저장하는 방식을 채택해보았다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, K = map(int, input().split())

memo = [0] * (K+1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    # 물건의 무게가 버틸 수 있는 무게보다 작다면 해당 무게에 가치를 저장한다.
    if W <= K:
        # 범위를 이렇게 설정한 이유는, 오름차순으로 하였을 때의 중복 덧셈 오류를 방지하기 위해서 이다.
        for idx in range(K-W, 0, -1):
            # if memo[idx] != 0:
            memo[idx+W] = max(V + memo[idx], memo[idx+W])
        # 이를 맨 마지막에 해주는 이유는 해당 물건을 두 번 가져가지 않기 위해서 이다.
        if memo[W] < V:
            memo[W] = V
ans = max(memo)
print(ans)

"""
-코드 리뷰-
: 내가 두시간동안 짠 알고리즘이 이미 존재하는 냅색알고리즘이라고 하더라..
뭔가 너무 허무했다.. 19번째 줄의 memo[idx] != 0 조건을 굳이 안 넣어도 결과는 똑같다고 한다.
"""