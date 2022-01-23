A = int(input())
B = int(input())
C = int(input())
cnt = 0
ABC = str(A*B*C)

for i in range(10):
    for j in list(ABC):
        if i == int(j):
            cnt += 1
    print(cnt)
    cnt = 0