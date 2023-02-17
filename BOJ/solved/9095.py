"""
기초적인 부분을 잊게 되는 것 같다.
factorial의 구현과 중복 원소들의 나열 방법들에서 조금 헤매다니.. 많은 실망을 하지 않을 수 없었고..
이를 방지하기 위해서는 꾸준함이 답인 것 같다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

T = int(input())

def factorial(num):
    global memo
    if num <= 1:
        return 1
    else:
        if memo[num] == 0:
            memo[num] = num * factorial(num - 1)
            return memo[num]
        else:
            return memo[num]

for tc in range(T):
    num = int(sys.stdin.readline())
    ans = 0

    memo = [0] * (num+1)

    a, b, c = 1, 2, 3
    for i in range(num+1):
        for j in range((num // b) + 1):
            for k in range((num // c) + 1):
                if (i * a) + (j * b) + (c * k) == num:
                    ans += factorial(i + j + k) // (factorial(i) * factorial(j) * factorial(k))
    
    print(ans)

"""
-코드 리뷰-
: 반복되는 규칙을 찾아 DP로 풀어내어 점화식을 도출해내는데..
많이 생각할 필요가 있다고 판단되었다.
"""