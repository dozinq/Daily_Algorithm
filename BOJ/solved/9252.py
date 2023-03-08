"""
얼마전에 LCS문제를 풀어봤던 경험이 있었는데 그때는 최장공통수열의 길이만을 도출해내는 것이었다면,
이번에는 최장공통수열이 무엇인지도 출력할 수 있었어야 했다.
숫자가 아닌 문자를 저장할 수 있도록 하여 풀이하였다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

word_1 = list(map(str, input()))
word_2 = list(map(str, input()))

data = [list('' for _ in range(len(word_2)+1)) for _ in range(len(word_1)+1)]

ans = ''
for i in range(1, len(word_1)+1):
    for j in range(1, len(word_2)+1):
        if word_1[i-1] == word_2[j-1]:
            data[i][j] = data[i-1][j-1] + word_1[i-1]
            if len(data[i][j]) > len(ans):
                ans = data[i][j]
        else:
            data[i][j] = data[i-1][j] if len(data[i-1][j]) > len(data[i][j-1]) else data[i][j-1]

if ans == '':
    print(0)
else:
    print(len(ans))
    print(ans)