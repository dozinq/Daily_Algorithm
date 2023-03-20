import sys
sys.stdin = open('BOJ/input.txt')

while True:
    tmp = sys.stdin.readline().strip()
    if tmp == 'end':
        break
    else:
        flag = [0, 1, 1]
        for i in range(len(tmp)):
            # 1. a, e, i, o, u를 포함하는지 검색.
            if tmp[i] in ('a', 'e', 'i', 'o', 'u'):
                flag[0] = 1
            # 2. 모음이 3번 연속인 경우, 자음이 3개 연속인 경우.
            if i < len(tmp)-2:
                if tmp[i] in ('a', 'e', 'i', 'o', 'u') and tmp[i+1] in ('a', 'e', 'i', 'o', 'u') and tmp[i+2] in ('a', 'e', 'i', 'o', 'u'):
                    flag[1] = 0
                    break
                elif tmp[i] not in ('a', 'e', 'i', 'o', 'u') and tmp[i+1] not in ('a', 'e', 'i', 'o', 'u') and tmp[i+2] not in ('a', 'e', 'i', 'o', 'u'):
                    flag[1] = 0
                    break
            # 3. 맨 마지막 단어를 제외하고, 연속된 단어가 나온다면 break
            if i < len(tmp)-1:
                if tmp[i] == tmp[i+1]:
                    if tmp[i] == 'e' or tmp[i] == 'o':
                        continue
                    flag = 0
                    break
        if flag == [1, 1, 1]:
            print(f'<{tmp}> is acceptable.')
        else:
            print(f'<{tmp}> is not acceptable.')