"""
직접 계산해보면서 풀이할 수 있었다.
많은 시간이 걸리긴하였지만, 알고리즘을 생각할 수 있었고
메모하는 방식으로 이전의 값을 저장하며 비교하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

data = [i for i in map(int, input().split())]
memo = [0]

for i in range(N):
    for j in range(len(memo)-1, -1, -1):
        if memo[j] < data[i]:
            if j == len(memo)-1:
                memo.append(data[i])
                break
            else:
                memo[j+1] = data[i]
                break
        # elif memo[j] == data[i]:
        #     memo[j] = data[i]

ans = len(memo)-1
# print(memo)
print(ans)