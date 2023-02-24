"""
그림으로 그려보고, 루트의 총 개수를 파악할 수 있었다.
처음에는 메모이제이션을 사용할까하다가 미래경로에 변수가 생긴다면 다시 갈아엎어야하는 상황이므로 내린 판단이었다.
그 결과, 총 루트는 6가지의 반복이다. 선택지는 총 3개. 0, 1, 2.
0-1, 0-2, 1-0, 1-2, 2-0, 2-1. 이렇게 총 6가지 루트가 존재하고,
매 반복문마다 이들의 합 중 끝날때의 위치가 같은 걸 비교하여 가장 효율적인 값을 저장해놓는다.
다음 인덱스에서는 끝날때의 위치를 통해 다시 6가지의 루트로 저장시키면 된다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

for idx in range(N-1):
    # 1-0과 2-0의 값을 비교하여 최솟값을 저장한다.
    data[idx+1][0] = min((data[idx][1] + data[idx+1][0]), (data[idx][2] + data[idx+1][0]))
    # 0-1과 2-1의 값을 비교하여 최솟값을 저장한다.
    data[idx+1][1] = min((data[idx][0] + data[idx+1][1]), (data[idx][2] + data[idx+1][1]))
    # 0-2와 1-2의 값을 비교하여 최솟값을 저장한다.
    data[idx+1][2] = min((data[idx][0] + data[idx+1][2]), (data[idx][1] + data[idx+1][2]))
print(min(data[-1]))

"""
-코드 리뷰-
: 내가 푼 방식이 곧 DP라고 한다.. 다들 나랑 똑같이 생각한다.. 나름 참신하다고 생각했는데..
"""