"""
탐색을 통해 논리적인 알고리즘을 구현할 수 있었는데,
시간 초과 오류가 발생하여 12865-1이라는 두번째 해결 방안을 떠올리게 되었다.
이는 pypy로 제출하여도 시간초과 오류가 발생한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def search(cnt, value):
    global visited, ans
    # data의 무게 순서대로 탐색할 것이며, idx란 무게를 의미한다.
    # K까지 탐색을 하되 현재 가지고 있는 무게를 제외한 목록에서 탐색을 해야하므로 다음과 같이 범위를 설정해주었다.
    for idx in range(1, K+1-cnt):
        if data[idx] != []:
            # 최소 탐색 범위를 length로 설정해주었다. 이 이상 탐색이 불가능하거나 무의미하다.
            length = min(K // idx, len(data[idx]))
            # 탐색 가능한 물건이 2개 이상이라면, 정렬해준다.
            if length >= 2:
                data[idx].sort()
            for i in range(0, length):
                if visited[idx] < i:
                    visited[idx] = i
                    search(cnt+idx, value+data[idx][i])
                    visited[idx] -= 1
    if ans < value:
        ans = value
    return

N, K = map(int, input().split())

data = [list() for _ in range(K+1)]
# 물건의 무게가 버틸 수 있는 무게보다 작다면 해당 무게에 가치를 저장한다.
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    if W <= K:
        data[W].append(V)

visited = [-1] * (K+1)
ans = 0
search(0, 0)
print(ans)