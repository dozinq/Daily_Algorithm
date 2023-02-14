# 간단하게 문제에서 말한 그대로를 전개해보았다.
# 뭔가 찝찝함이 있었던 건 사실이어서, 코드리뷰를 통해 개선하고자 하였다.

import sys
sys.stdin = open('../input.txt')

data = input()

if data == '1 2 3 4 5 6 7 8':
    print('ascending')
elif data == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')

"""
코드리뷰
: 다양한 답들이 있었는데, 대부분 나랑 비슷하게 푼 것으로 보인다만,
어떤 사람은 sorted를 이용해서 비교하면서 풀었던게 인상깊었다.

data = list(map(int, input().split()))
if data == sorted(data):
    print('ascending')
elif data == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

"""