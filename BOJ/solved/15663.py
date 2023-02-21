"""
원래는 내 방식대로 수련 겸 permutation 함수를 작성하여 문제에 맞는 결과가 나오도록 해봤는데,
시간 초과 에러를 벗어날 수 없었다.
permutations를 import 하는 상황을 최대한 피하고 싶었지만,
하루 동안 아무리 생각해봐도 코드를 개선하지 못하여 질문만 남긴 채로 마무리 지으려고 마음을 돌렸다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

from itertools import permutations

N, M = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

tmp = list(permutations(data, M))

ans = sorted(set(tmp))

for i in ans:
    print(*i)


# import sys
# sys.stdin = open('BOJ/input.txt')

# def permutation(num, cnt):
#     global ans, tmp, prev
#     if cnt == M:
#         perm = ' '.join(map(str, tmp))
#         ans.append(perm)
#         # t = tmp.copy()
#         # if t != prev:
#         #     ans.append(t)
#         #     # print(*t)
#         return
#     else:
#         for idx in range(len(data)):
#             if idx != num:
#                 tmp.append(data[idx])
#                 permutation(idx, cnt+1)
#                 tmp.pop()
#         return

# N, M = map(int, input().split())

# data = [i for i in map(int, sys.stdin.readline().split())]
# data.sort()
# ans = []

# for i in range(len(data)):
#     tmp = [data[i]]
#     permutation(i, 1)

# for i in sorted(set(ans)):
#     print(i)