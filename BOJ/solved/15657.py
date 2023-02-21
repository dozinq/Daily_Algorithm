"""
다른 문제들에 이어서 계속 백트래킹을 풀면서 백트래킹에 대한 이해도가 높아지고 있는 것 같다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def combination(idx):
    global ans
    if len(ans) == M:
        print(*ans)
        return
    else:
        for i in range(idx, len(data)):
            ans.append(data[i])
            combination(i)
            ans.pop()
        return

N, M = map(int, input().split())

data = [i for i in map(int, sys.stdin.readline().split())]
data.sort()

for i in range(len(data)):
    ans = [data[i]]
    combination(i)