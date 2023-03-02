"""
factorial을 구현하는건 재귀 함수의 연습과정이라 반가웠다.
그렇게 어렵지 않은 문제라고 생각되기는 했지만,
문제에 대한 이해가 쉽지 않았다.
"""


import sys
sys.stdin = open('BOJ/input.txt')

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

N = factorial(int(input()))

for i in range(len(str(N))):
    if N % 10 != 0:
        print(i)
        break
    else:
        N //= 10


"""
-코드 리뷰-
: 뒷자리가 0이 나오는 경우를 생각하여 5와 10의 존재를 확인하는 사람들을 봤다..
어떻게 이렇게 신박할까 싶었다. factorial의 구현은 어렵지 않으므로, 그런 경우도 있구나 생각만 해두어야겠다.
"""