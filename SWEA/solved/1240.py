import sys
sys.stdin = open('input.txt')

def check_password(lst):
    if (((lst[0] + lst[2] + lst[4] + lst[6])*3) + (lst[1] + lst[3] + lst[5]) + lst[7]) % 10 == 0:
        return sum(lst)
    return 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    my_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    ans_lst = []
    data = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1':
                for index in range(j-55, j-5, 7):
                    tmp = my_dict.get(data[i][index:index+7])
                    ans_lst.append(tmp)
            if len(ans_lst) > 0:
                break
        if len(ans_lst) > 0:
            break

    # for i in range(N):
    #     for j in range(M):
    #         if data[i].find('1'):
    #             if data[i][j:j+7] in my_dict:
    #                 for _ in range(8):
    #                     tmp = my_dict.get(data[i][j:j+7])
    #                     ans_lst.append(tmp)
    #                     j += 7
    #         if len(ans_lst) > 0:
    #             break
    #     if len(ans_lst) > 0:
    #         break

    print(f'#{tc} {check_password(ans_lst)}')
