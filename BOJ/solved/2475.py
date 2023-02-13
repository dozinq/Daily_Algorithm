data = list(map(int, input().split()))
memo = 0

for i in range(5):
    memo += data[i]**2

print(memo % 10)
