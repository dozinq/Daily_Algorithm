"""
메모를 해주면서 시간을 단축시키려고는 하였으나, 메모가 되지 않았을 경우는 O(N//2)만큼의 시간이 소요되므로,
DP를 통해 미리 메모를 해놓아야겠다고 생각하였다. 10942-1 이라는 이름의 파일로 재 작성하려 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def palindrome(start, end):
    head, rear = start, end
    while head < rear:
        # 이미 메모에 1로 기록되어 있다면,
        if memo[head][rear] == 1:
            return 1
        # 확인하는 부분의 앞 뒤가 다르다면,
        if data[head] != data[rear]:
            return 0
        else:
            head += 1
            rear -= 1
    # 팰린드롬이어서 위의 반복문을 통과했다면 메모해준다.
    while head >= start:
        memo[head][rear] = 1
        head -= 1
        rear += 1
    return 1

N = int(input())
data = list(map(int, input().split()))
memo = [list(0 for _ in range(len(data))) for _ in range(len(data))]

for _ in range(int(input())):
    tmp_1, tmp_2 = map(int, sys.stdin.readline().split())
    print(palindrome(tmp_1-1, tmp_2-1))
