"""
단순하게 정해진 범위 안에서 이동하면 될 줄 알고 구현하였으나, 인덱스 오류 발생.
반례를 생각해보니, 범위 밖의 다른 마을을 들러도 상관 없으니 완전히 틀린 답변이 되어버렸다.
이후 1916-1 이라는 이름의 다익스트라 알고리즘을 구현한 파일로 작업하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit = 1000000

def search(node, val):
    global ans
    stack = [node]

    while stack:
        tmp = stack.pop()
        if tmp == end:
            ans = min(ans, val)
            return
        else:
            for n in range(1, N+1):
                if data[tmp][n] < 100000 and val + data[tmp][n] < ans and n != tmp:
                    val = val + data[tmp][n]
                    stack.append(n)
                    val = val - data[tmp][n]
            return

    # if node == end:
    #     ans = min(ans, val)
    #     return
    # else:
    #     for n in range(1, N+1):
    #         if data[node][n] < 100000 and val + data[node][n] < ans and n != node:
    #             search(n, val+data[node][n])
    #     return

N = int(input())

tmp = []
for _ in range(int(input())):
    tmp.append(list(map(int, sys.stdin.readline().split())))

data = [list(100000 for _ in range(N+1)) for _ in range(N+1)]
for idx in tmp:
    data[idx[0]][idx[1]] = min(data[idx[0]][idx[1]], idx[2])

start, end = map(int, sys.stdin.readline().split())

# ans의 값을 최대치로 초기화해준다.
ans = 1000 * 100000

search(start, 0)
print(ans)

