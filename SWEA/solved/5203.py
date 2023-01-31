"""
느낀 점 -
1. 그 동안 나는 라이브러리를 필요로 하지 않으려고 애써봤다. 응 아니었다. 하나를 더 외우더라도, 아니. 외우자.
2. 방향이 중요한 것을 느꼈다. 얼마나 빨리 해결하는 지는 당장 나에게 중요한 것이 아니다. 문제를 해결하기 위해 정확한 해답을 내릴 수 있는 능력을 기르자.
"""

import sys
from itertools import combinations
sys.stdin = open('input.txt')

def babygin(player, lst):                               # 해당 게임의 player와 그의 카드목록을 인자로 받아 온다.
    global ans                                          # ans값은 전역에서 갱신될 수 있도록 한다.

    for index in range(len(lst)):                       # 카드목록의 조합들을 하나씩 살펴보게 한다.
        if lst[index][0] == lst[index][1] and lst[index][1] == lst[index][2]:   # triplet!
            ans = player
        else:
            tmp = sorted(lst[index])                            # 너무 억지스럽게 tmp라는 리스트 안에 현재 카드 목록의 조합 인덱스를 정렬한 값을 넣었다. (sort 메소드는 리스트만 사용가능하므로)
            if tmp[2] - tmp[1] == 1 and tmp[1] - tmp[0] == 1:   # 가장 큰 값 - 중간 값, 중간 값 - 가장 작은 값 모두 1이라면,
                ans = player                                    # run!
    return

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    lst_a = []
    lst_b = []
    ans = 0
    for i in range(12):
        if not i % 2:
            lst_a.append(data[i])                       # lst_a는 플레이어 1의 카드 목록이다.
        else:
            lst_b.append(data[i])                       # lst_b는 플레이어 2의 카드 목록이다.
        if i >= 4:                                      # 카드가 3장 이상을 받게 된다면 베이비진 조사가 가능하다!
            lst = list(combinations(lst_a, 3)) if not i % 2 else list(combinations(lst_b, 3))   # 현재 게임하는 플레이어의 카드목록을 조합시켜서 lst라는 리스트로 받아준다.
            babygin((i % 2) + 1, lst)                   # 현재 플레이어, 카드목록의 조합을 넘겨주고 babygin 실시!
            if ans > 0:                                 # ans 값이 바뀌었다면 탈출~~
                break

    print(f'#{tc} {ans}')