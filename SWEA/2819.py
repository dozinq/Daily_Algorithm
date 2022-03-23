# 임시 저장 변수를 리스트로 했는데 자꾸 오류를 만났었다. return의 개념을 아직 이해하지 못하고 있나보다

import sys
sys.stdin = open('input.txt')

def num_play(x, y, tmp):
    tmp += data[x][y]
    if len(tmp) == 7:                                               # 7자리 수라면,
        if tmp not in ans_lst:                                      # 그 수가 이미 등록되지 않았다면, 누적!
            ans_lst.append(tmp)
        return
    for i in range(4):
        if 0 <= x + delta[i][0] < 4 and 0 <= y + delta[i][1] < 4:   # 재귀~~
            num_play(x+delta[i][0], y+delta[i][1], tmp)

T = int(input())

for tc in range(1, T+1):
    data = [list(input().split()) for _ in range(4)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]                      # 상하좌우
    ans_lst = []                                                    # 답을 담을 리스트 생성
    for i in range(4):
        for j in range(4):
            tmp = ''                                                # 문자열로 임시 저장 변수 선언
            num_play(i, j, tmp)
    print(f'#{tc} {len(ans_lst)}')