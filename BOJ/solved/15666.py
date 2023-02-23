"""
tmp 변수로 숫자를 저장하여 비교하는 방식을 채택하여 구현해 보았는데, 출력초과 오류가 발생하였다.
아무리 생각해봐도 틀린 이유를 모르겠었는데 괜한 시도를 한 것 같아 문제에서 의도한대로 리스트 형식을 활용하여 문제를 해결할 수 있었다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

def combination(cnt):
    global prev, tmp
    if cnt == M:
        # if prev < tmp:
            print(' '.join(map(str, tmp)))
            # prev = tmp
            return
    else:
        for idx in data:
            if cnt == 0 or tmp[-1] <= idx:
                tmp.append(idx)
                combination(cnt+1)
                tmp.pop()


N, M = map(int, input().split())
data = sorted(list(set(map(int, sys.stdin.readline().split()))))

prev = 0
tmp = []

combination(0)

