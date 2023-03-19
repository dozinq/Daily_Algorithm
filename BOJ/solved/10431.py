import sys
sys.stdin = open('BOJ/input.txt')

P = int(input())

for _ in range(P):
    data = list(map(int, sys.stdin.readline().split()))

    lst = [data[1]]
    ans = 0
    for idx in range(2, 21):
        lst.append(data[idx])
        for stu in range(len(lst)):
            if lst[stu] > data[idx]:
                tmp = data[idx]
                while stu < len(lst):
                    lst[stu], tmp = tmp, lst[stu]
                    if stu == len(lst)-1:
                        break
                    stu += 1
                    ans += 1
                break
    print(data[0], ans)