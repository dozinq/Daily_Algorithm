"""
sort 메소드를 사용하면 메모리 초과 및 시간 초과.
아이디어가 떠오르지 않아, 구글링 후 계수정렬에 대해 배우고 다시 작성하였다.
시간 초과를 막기 위해 추가적으로 input() 대신 sys.stdin.readline()으로 대체하여 입력시간을 최소화하였다.
"""
import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = [0] * 10001

for _ in range(N):
    tmp = int(sys.stdin.readline())
    data[tmp] += 1

for idx in range(1, 10001):
    if data[idx] != 0:
        for _ in range(data[idx]):
            print(idx)