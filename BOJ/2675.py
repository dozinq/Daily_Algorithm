T = int(input())

for _ in range(T):
    R, S = input().split()
    for index in S:
        print(index * int(R), end = '')
    print()