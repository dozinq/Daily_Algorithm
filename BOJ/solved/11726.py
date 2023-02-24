"""
아직까지는 알고리즘의 구현이라기보다는 문제를 해결하기 위한 답안을 찾아내고,
그것을 가장 효율적으로(간단하게) 설계해야 하는 수준이라고 생각된다.
그 점에 있어서 아직까지는 좀 재미없다고도 생각된다.
얼른 알고리즘을 배우고 그를 활용하는 문제를 만나고 싶다.
다만, 아직 내 실력 자체가 많이 재미없는 수준에서 벗어나지 못하는 것 같기도 하다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

# 1: 1, 2: 2, 3: 3, 4: 5, 5: 8. 즉, n == (n-2) + (n-1)이다.
# def tiling(num):
#     if num <= 2:
#         return data[num]
#     else:
#         return tiling(num - 1) + tiling(num - 2)


n = int(input())
data = list(0 for _ in range(n+2))
data[1] = 1
if n >= 2:
    data[2] = 2
if n >= 3:
    for idx in range(3, n + 1):
        data[idx] = data[idx - 1] + data[idx - 2]

print(data[n] % 10007)
