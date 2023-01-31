import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = [[] for _ in range(N)]
    a = 0           # 반복문 시행할 때마다 시행 횟수는 1씩 증가하게 한다.
    print(f'#{tc}')
    for index in range(N):
        a += 1
        for num in range(1, a+1):
            if num == 1:                    # 각 행의 시작은 항상 1이다.
                num_lst[index].append(1)
            elif num == a:                  # 각 행의 끝은 항상 1이다.
                num_lst[index].append(1)
            else:                           # 이전 행의 전 자리의 수 + 이전 행의 해당 자리의 수
                num_lst[index].append(num_lst[index-1][num-2] + num_lst[index-1][num-1])
            print(num_lst[index][-1], end=' ')  # 출력방식을 이렇게 반복문이 시행될 때마다 해 줌으로써
        print()                                 # 코드의 길이를 더 줄일 수 있다.