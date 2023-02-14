"""
멍청하게 풀었던 것 같다. 리스트로 처리하였으면 조금 더 깔끔하였을 것으로 판단된다.
"""

import sys
sys.stdin = open('../input.txt')

# 0 0 0 이 입력된다면 종료. -> while
while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')

"""
-코드 리뷰-
while True:
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break
    # sort 메소드를 통해 정렬한다.
    data.sort()
    if data[2] ** 2 == data[1] ** 2 + data[1] ** 2:
        print('right')
    else:
        print('wrong')
"""