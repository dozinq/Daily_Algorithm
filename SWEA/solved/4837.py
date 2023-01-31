import sys
sys.stdin = open('input.txt')

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]     # 1~12 원소를 가지고 있는 리스트 생성

for tc in range(1, T+1):
    N, K = map(int, input().split())            # N, K를 입력받는다.
    ans = 0                                     # K가 어느 만큼 나오는지 셀 변수이다.
    for num in range(1, 1 << len(A)):           # 부분집합을 구할 때와 같이 구현하였다.
        tmp_lst = []                            # 매 탐색마다 비교 리스트는 초기화된다.
        for j in range(len(A)):
            if num & (1<<j):
                tmp_lst.append(A[j])            # 매번 부분집합을 생성할 수 있게 한다.
        if len(tmp_lst) == N:                   # 만들어진 부분집합의 원소의 수가 N과 같다면,
            if sum(tmp_lst) == K:               # 그리고, 그 원소들의 합이 K라면,
                ans += 1                        # 구하고자 하는 ans는 1씩 누적되게 한다.

    print(f'#{tc} {ans}')