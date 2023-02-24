"""
코드리뷰를 마친 지금에야 이게 이분탐색 문제인줄은 알지만, 그 개념을 모르고 풀이하다보니
조건을 설정해주는 부분에서 많은 시행착오를 겪어야만 하였다.
결론은 이분탐색을 사용하지 않고 누적합으로 풀이가 가능하였다.
코드리뷰를 통해 이분탐색에 대해 알 수 있었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

# 데이터 입력 받는다.
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)
data.append(0)

arr = [0 for _ in range(N+1)]
# 각 인덱스 마다의 차이값과 인덱스값을 곱하고 이전 값에 누적하여 더해준다.
# 이는 높이당 자를 수 있는 나무의 수를 의미할 것이다.
for idx in range(1, len(arr)):
    arr[idx] = arr[idx-1] + (idx * (data[idx-1] - data[idx]))
    if idx == len(arr)-1:
        arr[idx] = arr[idx-1] + (idx * data[idx-1])

ans = data[0] - M

for idx in range(1, len(arr)):
    if M == arr[idx]:
        ans = data[idx]
        break
    elif M < arr[idx]:
        ans = data[idx-1]
        # 이때의 높이는 data로 입력받은 idx의 길이 - 몫이다. 나머지가 있다면 몫 + 1을 차감해주어야 한다.
        if (M - arr[idx-1]) % idx != 0:
            ans -= ((M - arr[idx-1]) // idx) + 1
            break
        else:
            ans -= ((M - arr[idx-1]) // idx)
            break
print(ans)

"""
-코드 리뷰-
: 이진 탐색을 이용한 풀이방법을 복습해 보았다.

N, M = map(int, input().split())
data = list(map(int, input().split()))
start, end = 1, sum(data)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in data:
        if i > mid:
            cnt += i - mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

"""

