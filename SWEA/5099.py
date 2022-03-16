"""
문제점 : 스스로가 생각하기에도 너무 복잡하게 엉터리 코드를 만들었다. 난 발전해야 한다.
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    fire = [0] * N
    num_lst = [0] * N
    flag = 0

    while(flag == 0):                           # 탈출조건을 생각하다 flag라고 하기로 하였음.
        for i in range(N):                      # 화로가 돌아가는 것과 동일하게 생각하기 위해 반복문 for 사용
            if fire[i] != 0:                    # 현재 화로의 위치가 피자가 있다면 
                if fire[i] // 2 > 0:            # 치즈를 1/2 시켜준다.
                    fire[i] //= 2
                else:                           # 그 결과값이 0보다 작다면 0으로 만들어준다.
                    fire[i] = 0
                    num_lst[i] = 0              # num_lst : 현재 화로의 위치에, 몇번째 피자가 위치하는지 저장해놓은 변수
            if fire[i] == 0 and len(data) > 0:          # 현재 화로 위치가 비어있고 피자 여분이 있을때,
                pizza = data.pop(0)                     # 피자를 지목하고,
                fire[i] = pizza                         # 현재 화로의 위치에 피자를 집어 넣는다.
                num_lst[i] = M - len(data)              # 그때, 몇번째 피자를 넣은 것인지 인덱스값을 적는다.

            if len(data) == 0 and fire.count(0) == N-1: # 피자가 더 이상 없고, 빈 화로의 수가 1개를 제외하고 나머지가 될 때,
                flag = 1                                # flag(while 탈출조건)를 1로 설정하고,
                break                                   # for문을 탈출한다. (이후 flag로 인해, while문도 탈출시킨다.)
    for i in num_lst:       # num_lst는 현재 몇번째 피자만 화로에 있는지 저장되어 있는데 그 값을 찾아낸다.
        if i > 0:
            ans = i

    print(f'#{tc} {ans}')