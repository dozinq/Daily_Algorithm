"""
일단, 먼저 combination을 직접 구현해보았으나, 굉장히 큰 수를 찾아내는 데 있어서 많은 시간이 걸림을 알 수 있었고,
수학적으로 nCr == n! // {(n-r)! * r!} 이므로 팩토리얼을 구현하여 답을 찾아낼 수 있었다.
이 또한 팩토리얼을 math 라이브러리에서 가져올 수 있었지만, 메모이제이션을 사용한 팩토리얼로 직접 구현해보았다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

# def combination(num, cnt):
#     global data, ans
#     if cnt == m:
#         ans += 1
#     else:
#         for idx in range(num+1, n+1):
#             data.append(idx)
#             combination(idx, cnt+1)
#             data.pop()

def factorial(num):
    if num <= 1:
        return memo[num]
    else:
        if memo[num] != 0:
            return memo[num]
        memo[num] = num * factorial(num - 1)
        return memo[num]


n, m = map(int, input().split())
# cnt = 0
# ans = 0
# for i in range(1, n+1):
#     data = [i]
#     combination(i, 1)
# print(ans)
data = [i for i in range(1, n+1)]
memo = [0 for _ in range(n+1)]
memo[0], memo[1] = 1, 1

ans = factorial(n) // (factorial(n - m) * factorial(m))
print(ans)

"""
-코드 리뷰-
: 하나같이 죄다 math 라이브러리를 사용한 코드였다.
이래서는 내 실력에 대한 발전은 없을 것 같았고, 팩토리얼을 상향식으로 구현한 코드가 있어 복습해보았다.

def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

n, m = map(int, input().split())
print(fac(n) // (fac(m) * fac(n-m)))
"""