"""
메모지에 따로 그리지 않고 구현할 수 있을 것 같아서 먼저 의식의 흐름으로 코딩했었다.
딕셔너리를 구현하기도 하였고 복잡하게 생각하였다.
내가 뭔지 모르게 이상한 길로 빠져들고 있다고 생각이 들었을 때,
메모지에 다시 그려보니 생각보다 너무 단순한 식이 세워졌었다.
쓸데없이 너무 어렵다고만 생각했었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

# def factorial(num):
#     global memo

#     if num <= 1:
#         return 1
#     elif memo[num] != 0:
#         return memo[num]
#     else:
#         memo[num] = num * factorial(num - 1)
#         return memo[num]

T = int(input())

for _ in range(T):
    num = int(input())

    closet = []
    closet_kinds = []
    
    for _ in range(num):
        tool, kind = sys.stdin.readline().strip().split()
        if kind in closet_kinds:
            idx = closet_kinds.index(kind)
            closet[idx] += 1
        else:
            closet.append(1)
            closet_kinds.append(kind)
    
    ans = 1
    for idx in closet:
        ans *= (idx + 1)
    print(ans - 1)
