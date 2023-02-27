"""
나름 시간초과를 우려하여 dict와 list를 섞어서 풀이해보았다.
통과였고, 다른 사람들은 이렇게 풀지 않았을 거라 생각하고 코드 리뷰를 진행해보았다.
다들 set을 이용하여 교집합으로 풀던데.. 나로서는 이 생각을 한다는게 쉽지가 않았다.
다시 한번 배우게 되었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

data = {}
ans = []

for idx in range(N):
    tmp = sys.stdin.readline().strip()
    data[tmp] = 1

for idx in range(M):
    tmp = sys.stdin.readline().strip()
    if data.get(tmp) == 1:
        ans.append(tmp)

print(len(ans))
for i in sorted(ans):
    print(i)
