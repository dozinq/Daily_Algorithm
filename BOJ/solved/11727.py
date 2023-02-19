"""
규칙을 찾으려고 직접 많이 그려보았던 것 같다.
이때에 주의해야 할 점은, '규칙을 찾으려는 의도로 그려내야 한다'는 것이었다.
가로의 길이가 1씩 늘어나는 것이므로, n-1일때의 상황을 그대로 이어가면서,
어떤 부분이 더 추가되었는지를 n-2에서 추가하면서 생각하면 찾을 수 있다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

n = int(input())

data = list(0 for _ in range(n+1))

data[1] = 1

if n >= 2:
    data[2] = 3
if n > 2:
    for idx in range(3, n+1):
        data[idx] = data[idx - 1] + 2 * data[idx - 2]

print(data[n] % 10007)