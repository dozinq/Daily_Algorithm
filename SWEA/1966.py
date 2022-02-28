T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.sort()

    print('#%d' %tc, end=' ')
    for index in range(N):
        print('%d' %num_lst[index], end= ' ')
    print()