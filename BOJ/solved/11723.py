"""
시간 초과나 메모리 오류가 날 줄 알았지만, 통과되었다.
좀 뭔가 이상한 거 같아서 구글링 해 본 결과 원래는 set을 이용해서 풀어야 한다고 하더라.
또한 그 중에서도 set의 메소드에는 discard가 존재하는데, 이는 존재하지 않음을 보장하고 오류를 내지 않고 있을 시 삭제해주는 메소드라고 한다는 걸 배웠다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

M = int(input())
S = []

for _ in range(M):
    data = sys.stdin.readline().strip()
    if data[0:3] == 'add':
        num = int(data[4:])
        if num not in S:
            S.append(num)
    elif data[0:3] == 'rem':
        num = int(data[7:])
        if num in S:
            S.remove(num)
    elif data[0:3] == 'che':
        num = int(data[6:])
        if num in S:
            print(1)
        else:
            print(0)
    elif data[0:3] == 'tog':
        num = int(data[7:])
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif data[0:3] == 'all':
        S = [i for i in range(1, 21)]
    elif data[0:3] == 'emp':
        S = []