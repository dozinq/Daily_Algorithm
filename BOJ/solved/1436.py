"""
순열을 이용하여 10000가지의 경우의 수를 전부 구하려고 하였지만,
당연하게도 매우 비효율적이라는 생각이 들었다.(..구현도 쉽지는 않다)
다른 사람들의 코드를 보고 배운 결과.. 쉽게 생각하는게 맞다. => 브루트포스
(난이도가 낮은 문제는 빨리빨리 풀 생각을 하자.)
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

num = 666
count = 0
while True:
    if '666' in str(num):
        count += 1
    if count == N:
        print(num)
        break
    num += 1