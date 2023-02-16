"""
당연히 적은 수행시간이 주어져서 memoization을 사용한다고 생각은 했었지만,
일단 fibonacci를 재귀형 함수로 만들어서 실행해보았었고,
시간을 줄이기 위하여 memoization으로 내 식대로 만들어보았다.
많이 헤매긴 하였지만, 효율적으로 만든 거 같아서 뿌듯하다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def fibonacci(num):
    global memo

    for n in range(cnt, num+1):
        memo[n][0] = memo[n - 1][0] + memo[n - 2][0]
        memo[n][1] = memo[n - 1][1] + memo[n - 2][1]
    return

T = int(input())
# memo라는 2차원 배열을 통해 값을 저장할 수 있도록 한다.
memo = list([0 for _ in range(2)] for _ in range(41))
memo[0][0], memo[1][0], memo[0][1], memo[1][1] = 1, 0, 0, 1
cnt = 2

for tc in range(T):
    tmp = int(sys.stdin.readline().strip())
    if tmp < cnt:
        print(f'{memo[tmp][0]} {memo[tmp][1]}')
    else:
        fibonacci(tmp)
        print(f'{memo[tmp][0]} {memo[tmp][1]}')
        cnt = tmp
