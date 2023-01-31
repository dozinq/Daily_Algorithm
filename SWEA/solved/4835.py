T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 정수 입력받기
    num_lst = list(map(int, input().split()))
    sum_num = 0
    max_sum_num = 0
    for index in range(0, N-M+1):
        for num_index in range(index, index+M):
            sum_num += num_lst[num_index]
        if max_sum_num <= sum_num:
            max_sum_num = sum_num
        sum_num = 0

    min_sum_num = max_sum_num
    for index in range(0, N-M+1):
        for num_index in range(index, index+M):
            sum_num += num_lst[num_index]
        if min_sum_num >= sum_num:
            min_sum_num = sum_num
        sum_num = 0

    print('#{} {}' .format(tc, (max_sum_num - min_sum_num)))