"""
N의 분해합이 주어진 수보다 작다면 반복문을 종료하려고 조건을 걸었는데,
생각해보니 숫자가 작아진다해서 분해합도 작아지는건 아니어서 조금 헤맸던 것 같다.
다른 사람들의 코드리뷰를 보니, 조건문의 숫자를 증가하는 방식으로 해결하더라.
"""

import sys
sys.stdin = open('../input.txt')

# 주어진 수에서 1씩 차감하면서 생성자인지 확인한다.
# N의 분해합이 주어진 수보다 낮다면 ans를 출력한다. => ?

ans = 0
data = int(input())
for num in range(data, 0, -1):
    temp = num
    ans_tmp = num
    while num:
        temp += num % 10
        num //= 10
    if temp == data:
        ans = ans_tmp

print(ans)
