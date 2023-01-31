T = int(input())

for tc in range(1, T+1):
    num = int(input())
    num_lst = list(map(int, input().split()))

    max_num = 0
    for index in range(num):
        if num_lst[index] >= max_num:
            max_num = num_lst[index]

    min_num = max_num
    for index in range(num):
        if num_lst[index] <= min_num:
            min_num = num_lst[index]

    print('#{} {}'.format(tc, (max_num - min_num)))