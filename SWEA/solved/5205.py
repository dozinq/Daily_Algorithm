"""
느낀 점 -
1. 어제 병합정렬을 구현할 때는, 정말 내가 이해력이 부족한가 생각을 많이 했던 것 같다.
-> 그러다 퀵정렬을 만나니깐 너무 위로가 되는 것 같다. 퀵정렬 사랑해!
2. 퀵정렬의 간단한 이해가 필요해서 어제 학습내용을 참고했었다.
-> 퀵정렬은 pivot이 있는 정렬이라고 간단하게 생각하려 한다.
"""

import sys
sys.stdin = open('input.txt')

def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = []
    equal = []
    right = []
    for i in range(len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] == pivot:
            equal.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
    return quick(left) + equal + quick(right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans_lst = quick(data)
    print(f'#{tc} {ans_lst[N//2]}')