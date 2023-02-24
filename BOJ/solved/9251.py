"""
Longest Common Subsequence. LCS를 구하는 방법에 대한 생각을 많이 해봤던 것 같다.
2차원 배열에서 row부분은 첫번째 단어, col부분은 두번째 단어를 배치하였고,
이들을 비교해가면서 배열을 채워갈때의 규칙을 찾아가기 시작했다.
현재 인덱스의 문자가 일치한다면 [idx-1][idx-1]에서 +1한 값을 입력하면 되고,
아니라면 [idx-1][idx]와 [idx][idx-1]의 크기를 비교하여 더 큰 값을 입력하면 된다.
"""
import sys
sys.stdin = open('BOJ/input.txt')

def LCS():
    global data
    for idx_a in range(1, len(word_a)+1):
        for idx_b in range(1, len(word_b)+1):
            if word_a[idx_a-1] == word_b[idx_b-1]:
                data[idx_a][idx_b] = data[idx_a-1][idx_b-1] + 1
            else:
                data[idx_a][idx_b] = max(data[idx_a-1][idx_b], data[idx_a][idx_b-1])    
    return data[-1][-1]

word_a = input()
word_b = input()

data = [list(0 for _ in range(len(word_b)+1)) for _ in range(len(word_a)+1)]

print(LCS())