"""
문제에서 이항계수에 대한 설명이 따로 있지 않아 학습 후에 그대로 구현해보았다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N, K = map(int, input().split())

n_factorial = 1
k_factorial = 1
n_k_factorial = 1

for idx in range(1, N+1):
    n_factorial *= idx

for idx in range(1, K+1):
    k_factorial *= idx

for idx in range(1, N-K+1):
    n_k_factorial *= idx

print(n_factorial // (k_factorial * n_k_factorial))

"""
-코드 리뷰-
: 팩토리얼을 재귀 함수화하여 정의하고 문제를 간단하게 풀어내어 학습한 결과를 구현해보았다.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

"""