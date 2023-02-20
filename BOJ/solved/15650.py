from operator import index
"""
역시 반복된 연습만이 내 실력이 되는 것 같다.
이제는 그래도 조금 머릿속으로 알고리즘에 대해 생각하면서 작성하게 되는 것 같아 매우 뿌듯하다.
이는 순열로써, 중복된 숫자가 아닌 숫자의 순서를 출력하면 되는 문제이다.
nPr 에서 r은 cnt로 처리할 수 있도록 하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def permutation(num, cnt):
    global ans
    if cnt == M:
        print(*ans)
        return
    else:
        if num+1 <= N:
            for idx in range(num+1, N+1):
                ans.append(idx)
                permutation(idx, cnt+1)
                ans.pop()
    return

N, M = map(int, input().split())

for i in range(1, N+1):
    ans = [i]
    permutation(i, 1)