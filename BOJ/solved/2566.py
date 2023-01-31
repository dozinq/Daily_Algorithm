# 한 번 틀림. -> 모든 수가 0일 수도 있는 상황인데 고려하지 않았음.
# 문제를 꼼꼼히 읽어서 히든 케이스의 입력에도 대비할 수 있도록 연습하자.

import sys
sys.stdin = open('../input.txt')

ans_num = 0
ans = [1, 1]

for i in range(1, 10):
    data = list(map(int, input().split()))
    for j in range(1, 10):
        if ans_num < data[j - 1]:
            ans_num = data[j - 1]
            ans[0] = i
            ans[1] = j

print(ans_num)
print(f'{ans[0]} {ans[1]}')


# 코드 리뷰
# 2차원 배열로 받는다면 memory 소모가 있음. -> 위처럼, for문으로 비교 갱신해가면서 처리하는 방법이 memory를 아낄 수 있을 것이다.
# ans_num = 0
# x = y = 0
#
# for i in range(9):
#     data = list(map(int, input().split()))
#     if max(data) > ans_num:
#         ans_num = max(data)
#         x = i + 1
#         # index 메소드를 이용해서 index를 추출해내는 방법이 있다.
#         y = data.index(ans_num) + 1
#
# print(ans_num)
# print(x, y)