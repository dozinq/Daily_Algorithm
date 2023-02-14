"""
N은 주어지는 수, r = 3 인 조합을 만들어서 M에 가까운 수를 출력한다.
추가적으로, M이 나왔다면 바로 출력 가능하도록 하여 실행시간을 최소화하자.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def combine(index, check_r):
    global ans
    box.append(data[index])
    if check_r == 3:
        # 3개의 카드를 골랐다면, 합을 ans 변수와 비교하여 저장시킨다.
        if sum(box) > ans and sum(box) <= M:
            ans = sum(box)
        return
    else:
        for i in range(index, N, 1):
            # 인덱스 오류 방지를 위한 설정 <- i + 1 을 위해 방지해주었다.
            if i + 1 < N:
                combine(i + 1, check_r + 1)
                box.pop()

N, M = map(int, input().split())

data = list(map(int, input().split()))

r = 3

ans = 0

for idx in range(N):
    box = []
    combine(idx, 1)
    if ans == M:
        break

print(ans)

"""
-코드 리뷰-
: 실행시간을 고려하지 않는다면, 완전 탐색 방법으로 빠른 해결이 가능하다.

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                ans = max(result, arr[i] + arr[j] + arr[k])
print(ans)
"""

"""
조합 구현에 대한 복습 ex) nCr = 3C2

def DFS(L, BeginWith):

    # 종료조건
    if L == r:
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[L] = n[i]
            DFS(L + 1, i + 1)

n = [1, 2, 3]
r = 2

result = [0] * r

DFS(0, 0)


"""