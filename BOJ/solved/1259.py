"""
문자열 슬라이싱을 이용하여 풀 수 있었다.
나름 pythonic 하게 풀 수 있었던 것 같다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

while True:
    tmp = input()
    if tmp == '0':
        break
    data_asc = int(tmp)
    data_desc = int(tmp[::-1])
    if data_asc == data_desc:
        print('yes')
    else:
        print('no')

"""
-코드 리뷰-
: 다른 사람들은 더 간단하게 풀었다. 효율이 좋으니 복기해본다.
굳이 문자열을 숫자형으로 바꾸려고 하지 않고 그대로 풀었다는게 생각의 전환인 것 같다.

while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')

"""