"""
유니코드 숫자 반환 함수인 ord()를 기억할 수 있도록 하자.
"""

import sys
sys.stdin = open('BOJ/input.txt')

L = int(input())
data_tmp = input()

data = [0] * L
for i in range(L):
    # ord는 문자에 대응하는 유니코드 숫자를 반환한다. 97~122
    data[i] = ord(data_tmp[i])-96

ans = 0
for i in range(L):
    ans += data[i] * 31 ** i

print(ans % 1234567891)

"""
-코드 리뷰-
: 보다 간단하게 작성한 코드를 볼 수 있었다.
L = int(input())
data = input()
ans = 0

for i in range(L):
    ans += (ord(data[i]) - 96) * 31 ** i

print(ans % 1234567891)

"""