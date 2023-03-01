"""
각 가정마다 치킨집과의 최소거리를 구하고, 이를 임시 총합 변수에 저장해주었다.
그리고 이들의 합을 ans라는 변수 안에 최솟값을 찾아 저장해주었다.
또한, 치킨집들의 선택은 combinations로 해결할 수 있었다.
"""

from itertools import combinations
import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

data = []
houses = []
chicks = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            houses.append([i, j])
        if tmp[j] == 2:
            chicks.append([i, j])
    data.append(tmp)

ans = 10**10
for chick in combinations(chicks, M):
    total_tmp = 0
    for house in houses:
        min_dist = 1000
        for chi in chick:
            min_dist = min(min_dist, (abs(house[0] - chi[0]) + abs(house[1] - chi[1])))
        total_tmp += min_dist
    ans = min(ans, total_tmp)
print(ans)
