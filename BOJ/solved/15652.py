"""
문제를 읽어보고, 중복조합의 구현이라는 것을 알았다.
사실 순열과 조합의 개수를 구하는 공식은 알지만, '중복조합의 공식은?'이라는 물음에 즉각적으로 대답하길 스스로가 원하질 않는다.
코드상으로 구현해보니 나름 생각하면서 작성하는 거라 재미있다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def combination(num, cnt):
    global ans
    if cnt == M:
        print(*ans)
        return
    else:
        for idx in range(num, N+1):
            ans.append(idx)
            combination(idx, cnt+1)
            ans.pop()
        return

N, M = map(int, input().split())

for i in range(1, N+1):
    ans = [i]
    combination(i, 1)

"""
-코드 리뷰-
: 다른 사람들의 코드를 보니 나와 비슷한 것 같다.
다만, 조금 더 간단히 한다면, 변수 cnt를 따로 만들지 않고도 len()함수를 사용하여 클린 코드를 작성할 수 있다.
"""