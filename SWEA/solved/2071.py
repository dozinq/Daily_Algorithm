# import sys
# sys.stdin = open('input.txt')

T = int(input())        # 테스트 케이스의 개수 입력받기

for tc in range(1, T+1):        # 테스트 케이스의 수만큼 반복문 실행
    my_sum = 0                  # 인덱스마다 값을 누적시킬 변수상자 생성
    my_index = 0                # 인덱스의 개수를 셀 변수상자 생성
    my_lst = list(map(int, (input().split())))      # 입력받아 리스트로 저장
    for index in my_lst:        # 리스트에서 각 항목을 살펴본다.
        my_sum += index         # 각 항목의 값을 누적시킨다.
        my_index += 1           # 반복문이 실행될 때마다 개수를 셈한다.
    ans = round(my_sum/my_index)        # 평균값을 구하고 소수 첫째자리에서 반올림하여 저장한다.

    print('#{} {}'.format(tc, ans))     # 출력시키자!