import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())                                               # 매번 tc 숫자를 입력받는다.
    Arr = [list(map(int, input().split())) for _ in range(100)]     # 100*100 행렬을 입력받는다.
    ans = 0
    sum_tmp = 0
    for i in range(len(Arr)):                                       # 100을 range(len(Arr))로 대체해서 범위를 지정하였다.
        for j in range(len(Arr)):                                   # 2중 반복문 구조로 다음을 수행한다.
            sum_tmp += Arr[i][j]                                    # 각 행의 합을 누적시키고,
        if ans < sum_tmp:                                           # 최대값을 갱신시킨다.
            ans = sum_tmp
        sum_tmp = 0                                                 # sum_tmp 상자는 매번 초기화 시켜준다.
    for j in range(len(Arr)):
        for i in range(len(Arr)):
            sum_tmp += Arr[i][j]                                    # 각 열의 합을 누적시키고,
        if ans < sum_tmp:                                           # 최대값을 갱신시킨다.
            ans = sum_tmp
        sum_tmp = 0                                                 # sum_tmp 상자는 매번 초기화 시켜준다.
    for i in range(len(Arr)):                                       # (0,0) (1,1) ... (99,99) 까지 합을 구한다.
        sum_tmp += Arr[i][i]
    if ans < sum_tmp:                                               # 최대값을 갱신시킨다.
        ans = sum_tmp
    sum_tmp = 0                                                     # sum_tmp 상자는 다시 초기화 시켜준다.
    for i in range(len(Arr)):                                       # (0,99) (1,98) ... (99,0) 까지 합을 구한다.
        sum_tmp += Arr[i][99-i]
    if ans < sum_tmp:                                               # 최대값을 갱신시킨다.
        ans = sum_tmp
    print(f'#{tc} {ans}')