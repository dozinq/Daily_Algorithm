# import sys
# sys.stdin = open('input.txt')

data = list(map(int, input().split()))
ans = [0 for _ in range(6)]


for i in range(len(data)):
    if i <= 1:
        print(1 - data[i], end=" ")
    elif i == 5:
        print(8 - data[i], end=" ")
    else:
        print(2 - data[i], end=" ")

# for i in range(len(data)):
#     if i <= 1:
#         ans[i] = 1 - data[i]
#     elif i == 5:
#         ans[i] = 8 - data[i]
#     else:
#         ans[i] = 2 - data[i]


# 코드 리뷰 후 재작성

# data = [1, 1, 2, 2, 2, 8]
# input_data = list(map(int, input().split()))
# for i in range(6):
#     print(data[i] - input_data[i], end=" ")
