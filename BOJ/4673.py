lst = []

for i in range(1, 10001):
    num = i + ((i//10000)%10) + ((i//1000)%10) + ((i//100)%10) + ((i//10)%10) + (i%10)
    lst.append(num)

for i in range(1, 10001):
    if not i in lst:
        print(i)