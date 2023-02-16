"""
최대공약수와 최소공배수 문제를 가장 복잡하게 푼 사람이 나 일 거 같다.
소인수분해부터 최대한 구현해보려고 애썼고, 잘못 길을 들어왔다는 걸 알아차렸지만 돌아가기엔 구현하고 싶은 마음이 컸던 것 같아 끝까지 해보았다.
코드리뷰를 통해 더 손쉽게 구현할 수 있도록 할 것이다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

# 나머지가 1일때까지 약분해준다면, 소인수분해가 가능하다.
def mod1(num):
    box = []
    check = 2
    while True:
        if num == 1:
            break
        else:
            if num % check == 0:
                num //= check
                box.append(check)
            else:
                check += 1
    return box

# 최대공약수와 최소공배수를 구하는 함수의 구현
def max_min_check(box1, box2):
    global max_ans
    global min_ans

    for idx in a_and_b_box:
        if box1.count(idx) >= 1 and box2.count(idx) >= 1:
            max_ans *= idx ** min(box1.count(idx), box2.count(idx))
            min_ans *= idx ** max(box1.count(idx), box2.count(idx))
        elif box1.count(idx) >= 1 or box2.count(idx) >= 1:
            min_ans *= idx ** max(box1.count(idx), box2.count(idx))

    return

a, b = map(int, input().split())

# a, b의 소인수분해 결과값을 a_box, b_box에 담는다.
a_box = mod1(a)
b_box = mod1(b)

a_and_b_box = set(a_box + b_box)

max_ans = 1
min_ans = 1


max_min_check(a_box, b_box)

print(max_ans)
print(min_ans)

"""
-코드 리뷰-
: 다들 유클리드 호제법을 배우고, 그를 활용한 코드가 정말 많았는데..
사실 난 이 문제만을 풀기 위해 새롭게 뭘 더 배우는 건 비효율적이라고 생각하여
더 알기 쉽게 쓰여진 코드를 찾아보았다.
그 코드에서의 핵심은 최소공배수 == 최대공약수 * a를 최대공약수로 나눈 몫 * b를 최대공약수로 나눈 몫이라는
내가 잊고 있었던 수학적인 기본상식이었다.
이를 이용해 구현하면 다음과 같다.

a, b = map(int, input().split())

tmp = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        tmp.append(i)

print(max(tmp))
print(max(tmp) * (a // max(tmp)) * (b // max(tmp)))

"""