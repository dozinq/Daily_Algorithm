import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_str = input()
    my_lst = []
    for i in my_str:                                # str로 받은 값을 변경할 수 있도록 리스트로 처리한다.
        my_lst.append(i)
    pointer = 0
    while pointer < len(my_lst)-1:
        if my_lst[pointer] == my_lst[pointer+1]:    # 현재 검색중인 포인터값과 그 다음값이 동일하다면,
            my_lst.pop(pointer+1)                   # 포인터의 그 다음값과
            my_lst.pop(pointer)                     # 현재 포인터의 값을 날려버린다. -> 자동으로 다음 인덱스는 앞당겨진다!
            pointer = 0
        pointer += 1                                # 해당되지 않는다면 포인터는 다음 인덱스를 검색하도록 한다.
    print('#%d %d' % (tc, len(my_lst)))