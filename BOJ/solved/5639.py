"""
내가 한걸음 더 성장할 수 있으려면 재귀와 트리구조에 대한 완벽한 이해일 것이다.
아직은 트리구조가 익숙하지 않기도 하고, 재귀 구현이 머리아픈 일이기도 하다.
이 순회에서도 마찬가지였다. 재귀로 구현할때 어떤 방식으로 접근해야 할 지 잘 생각해보면서 작성해야 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')
sys.setrecursionlimit(1000000)

def binary_search(start, end):
    global ans
    if start > end:
        return
    mid = end+1
    for idx in range(start, end+1):
        if data[start] < data[idx]:
            mid = idx
            break
    
    binary_search(start+1, mid-1)
    binary_search(mid, end)
    ans.append(data[start])
    return

data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

ans = []
binary_search(0, len(data)-1)

for i in ans:
    print(i)