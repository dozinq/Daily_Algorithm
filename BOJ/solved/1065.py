N = int(input())

if N <= 99:
    print(N)
elif N >= 100:
    count = 99
    for i in range(100, N+1):
        num_str = str(i)
        num_1 = int(num_str[0])
        num_2 = int(num_str[1])
        num_3 = int(num_str[2])
        if num_2 - num_1 == num_3 - num_2:
            count += 1
    print(count)
