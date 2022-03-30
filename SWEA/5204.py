import sys
sys.stdin = open('input.txt')

T = int(input())

def merge_sort(lst):
    global cnt
    if len(lst) == 1:                           # 인자가 하나라면, 반환한다.
        return lst

    left = merge_sort(lst[:(len(lst) // 2)])    # 절반을 기준으로 왼쪽은 left라는 리스트로,
    right = merge_sort(lst[(len(lst) // 2):])   # 오른쪽은 right라는 리스트로 받는다.
    l_len = len(left)
    r_len = len(right)
    i = l_index = r_index = 0                   # i는 가리키는 인덱스의 위치, l_index와 r_index는 left와 right의 위치를 가리킨다.
    while l_index < l_len and r_index < r_len:  # left, right 둘 중 하나라도 정렬이 끝날 때까지 반복한다.
        if left[l_index] <= right[r_index]:     # 왼쪽이 더 작은 값을 가리킨다면,
            lst[i] = left[l_index]              # 인덱스는 그 값을 저장하고,
            l_index += 1                        # 왼쪽 인덱스는 하나 증가시킨다.
        else:
            lst[i] = right[r_index]             # 위와 같은 동작.
            lst[i] = right[r_index]
            r_index += 1
        i += 1                                  # 인덱스는 하나씩 늘어난다.

    if l_index == l_len:                        # 왼쪽이 먼저 정렬되었다면,
        for n in range(r_index, r_len):         # 오른쪽 남은 것들을 배정시킨다.
            lst[i] = right[n]
            i += 1
    elif r_index == r_len:                      # 오른쪽이 먼저 정렬되었다면,
        cnt += 1                                # cnt는 하나씩 증가하면서, 왼쪽 남은 것들을 배정시킨다.
        for n in range(l_index, l_len):
            lst[i] = left[n]
            i += 1

    return lst

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    ans_lst = merge_sort(data)
    print(f'#{tc} {ans_lst[N//2]} {cnt}')