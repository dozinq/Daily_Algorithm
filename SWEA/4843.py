import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))                               # num_lst를 입력받는다.
    for index in range(0, N):                                               # 정렬과정은 다음과 같다.
        if index % 2 == 0:                                                  # index가 짝수라면,
            for i in range(index, len(num_lst)):                            # 최대값을 index자리로 가져온다.
                if num_lst[index] < num_lst[i]:
                    num_lst[index], num_lst[i] = num_lst[i], num_lst[index]
        elif index % 2 == 1:                                                # index가 홀수라면,
            for i in range(index, len(num_lst)):                            # 최소값을 index자리로 가져온다.
                if num_lst[index] > num_lst[i]:
                    num_lst[index], num_lst[i] = num_lst[i], num_lst[index]

    print(f'#{tc}', end=' ')                    # 출력 - 앞의 10개만 할 수 있도록 한다.
    for index in range(10):
        print(f'{num_lst[index]}', end=' ')
    print()