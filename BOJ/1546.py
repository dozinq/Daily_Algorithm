N = int(input())
B = list()
A = list(map(int, input().split()))
for i in A:
    B.append((i/max(A))*100)
print(sum(B)/len(B))