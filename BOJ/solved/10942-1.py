"""
아무리 생각해봐도 DP가 더 빠를 순 없을 거라고 생각했지만, 모든 문제를 풀기위해서는
길더라도 단 한번 체크해놓는게 가장 낫다는 결론이 나왔다.
나름 많이 그려보면서 식을 수립하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = list(map(int, input().split()))
memo = [list(0 for _ in range(len(data))) for _ in range(len(data))]

for i in range(len(memo)):
    for j in range(len(memo)):
        # 대각선 방향으로 반복문을 수행한다.
        if i+j < len(memo):
            x, y = j, i+j
            if data[x] == data[y]:
                if x == y or x + 1 == y or x + 2 == y:
                    memo[x][y] = 1
                    continue
                if memo[x+1][y-1] == 1:
                    memo[x][y] = 1
                    continue

for _ in range(int(input())):
    tmp_1, tmp_2 = map(int, sys.stdin.readline().split())
    print(memo[tmp_1 - 1][tmp_2 - 1])