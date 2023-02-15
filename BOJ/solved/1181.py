"""
많은 수의 줄을 반복문을 통해 효율적으로 불러올 때 사용하는,
sys.stdin.readline() 은 하지만 개행문자까지 입력받는다.
이를 방지하기 위해, 문자열을 받아올때는 sys.stdin.readline().strip()을 통해
입력 받아야 한다.
"""

import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())
data = [[] for _ in range(50)]
# tmp_len = [[] for _ in range(50)]

for i in range(N):
    tmp = sys.stdin.readline().strip()
    data[len(tmp) - 1].append(tmp)
    # tmp_len[len(tmp[i])].append(i)
    # tmp_len[len(tmp[i])].append(i)

for i in range(50):
    if len(data[i]) != 0:
        for idx in sorted(set(data[i])):
            print(idx)


"""
-코드 리뷰-
: 이를 더 효율적으로 작성한 코드가 있어, 복습해보았다.
튜플 형식으로 저장한다는 것도 새로웠고, list(set(word))의 형식으로 다시 저장한다면 중복을 없애주는 것도 새로웠다.

n = int(input())

word = []
for i in range(n):
    word.append(input())

set_word = list(set(word))

sort_word = []
for i in set_word:
    sort_word.append((len(i), i))

ans = sorted(sort_word)

for len_word, word in ans:
    print(word)
"""