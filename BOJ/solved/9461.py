"""
어떤 규칙이 있는지 찾는다는 것은 늘 흥미로운 일이다.
또한 이를 이용해 나만의 식을 작성한다는 것 또한 그렇다.
간만에 매우 간결한 코드를 만든 것 같아 다행이다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def wave(num):
    global data
    if num <= 5:
        return data[num]
    else:
        if data[num] != 0:
            return data[num]
        else:
            data[num] = wave(num - 1) + wave(num - 5)
            return data[num]

T = int(input())
data = [0] * (101)
data[1], data[2], data[3], data[4], data[5] = 1, 1, 1, 2, 2

for _ in range(T):
    N = int(input())

    print(wave(N))


"""
-코드 리뷰-
: 역시 코드 리뷰를 안했었다면, 자만심에 빠지기 쉽다.
나는 좀 더 규칙을 확대하여 찾았었고, 원래는 n + 3 인덱스에는 n 인덱스와 n + 1 인덱스가 더한 값이 들어가면 된다.
"""
