import sys
sys.stdin = open("input.txt", "rt", encoding="utf-8")

for _ in range(10):
    tc = input()
    word = input()
    pile_str = input()

    ans = 0
    for i in range(len(pile_str)):
        tmp_ans = 0
        for j in range(len(word)):
            if pile_str[i] == word[j]:
                i += 1
                tmp_ans += 1
                if i >= len(pile_str):
                    break
        if len(word) == tmp_ans:
            ans +=1
    print(f'#{tc} {ans}')