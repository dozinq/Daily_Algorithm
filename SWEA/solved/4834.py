T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = int(input())
    num_lst = [0] * 10
    while(card > 0):
        index = card % 10
        card //= 10
        num_lst[index] += 1

    card_num = 0
    max_num = 0   # 0 0 0 0 1 0 1 1 0 0 2
    for index in num_lst:
        if max_num <= index:
            max_num = index
            ans_card_num = card_num
        card_num += 1

    print('#{} {} {}' .format(tc, ans_card_num, max_num))