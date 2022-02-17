import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ABC_lst = [input()for _ in range(100)]

    ABC_lst_col = []
    for i in range(100):
        tmp_str = ''
        for j in range(100):
            tmp_str += ABC_lst[j][i]
        ABC_lst_col.append(tmp_str)

    test_lst = []
    palindrome_lst = []
    ans = 0

    for i in range(100):
        for j in range(100):
            for N in range(100):
                if j+N <= 100:
                    tmp_str = ABC_lst[i][j:j+N]
                    if tmp_str == tmp_str[::-1]:
                        test_lst.append(len(tmp_str))
                    tmp_str = ABC_lst_col[i][j:j+N]
                    if tmp_str == tmp_str[::-1]:
                        test_lst.append(len(tmp_str))

    print(f'#{tc} {max(test_lst)}')