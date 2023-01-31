import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(10):
    tc, N = input().split()
    while(1):
        num_lst = list(map(str, input().split()))
        ten_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
        change_index = 0
        for num in ten_lst:
            for index in range(len(num_lst)):
                if num_lst[index] == num:
                    num_lst[change_index], num_lst[index] = num_lst[index], num_lst[change_index]
                    change_index += 1
        break
    print(tc)
    for i in num_lst:
        print(i, end=' ')
    print()