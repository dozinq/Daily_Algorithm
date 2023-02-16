"""
딕셔너리를 이용해서 풀어야겠다는 생각을 할 수 있었고,
다른 사람들의 코드 리뷰를 통해 풀이하는게 다 똑같다는 생각을 하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

data = {}
for _ in range(N):
    tmp_key, tmp_value = sys.stdin.readline().strip().split()
    data[tmp_key] = tmp_value

for _ in range(M):
    tmp = sys.stdin.readline().strip()
    print(data.get(tmp))