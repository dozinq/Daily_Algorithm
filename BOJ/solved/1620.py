"""
당연하게도 리스트를 이용해서 생각나는대로 코딩하였다가 시간 초과를 만나게 되었고, 조금 생각해보니
문제에 어울리게 딕셔너리를 이용해서 시간을 줄일 수 있다는 생각을 하게 되었고,
구현하게 되었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, M = map(int, input().split())

# data = [''] * (N+1)
# for idx in range(1, N+1):
#     data[idx] = sys.stdin.readline().strip()

# for _ in range(M):
#     tmp = sys.stdin.readline().strip()
#     if tmp in data:
#         print(data.index(tmp))
#     else:
#         print(data[int(tmp)])

data = {}
data_reverse = {}
for idx in range(1, N+1):
    data[idx] = sys.stdin.readline().strip()

for idx in range(len(data) + 1):
    data_reverse[data.get(idx)] = idx

for _ in range(M):
    tmp = sys.stdin.readline().strip()
    if tmp.isnumeric():
        print(data.get(int(tmp)))
    else:
        print(data_reverse.get(tmp))