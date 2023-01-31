# import sys
# sys.stdin = open('input.txt')

for tc_num in range(1, 11):
    len_tc = int(input())
    my_lst = list(map(int, input().split()))
    ans = 0
    for index in range(2, (len_tc - 2)):
        if my_lst[index] > my_lst[index-2] and my_lst[index] > my_lst[index-1]:
            if my_lst[index] > my_lst[index+1] and my_lst[index] > my_lst[index+2]:
                around_max = max(my_lst[index-2], my_lst[index-1], my_lst[index+1], my_lst[index+2])
                ans += my_lst[index] - around_max
            else:
                pass
        else:
            continue
    print('#{} {}'.format(tc_num, ans))
