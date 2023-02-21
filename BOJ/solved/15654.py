"""
순열을 구현하는 문제이다.
복잡하지 않아, 그리지 않고도 머릿속으로 생각하면서 구현할 수 있었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def permutation(idx):
    if len(ans) == M:
        print(*ans)
        return
    else:
        for i in range(len(data)):
            if data[i] not in ans:
                ans.append(data[i])
                permutation(i)
                ans.pop()
        return

N, M = map(int, input().split())
data = [i for i in map(int, input().split())]
data.sort()

for i in range(len(data)):
    ans = [data[i]]
    permutation(i)