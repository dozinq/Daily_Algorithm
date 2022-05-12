import sys
sys.stdin = open('input.txt')

S = input()
ans_lst = [0]*26
for i in range(len(S)):
    ans_lst[ord(S[i])-ord('a')] += 1

for i in ans_lst:
    print(i, end=' ')