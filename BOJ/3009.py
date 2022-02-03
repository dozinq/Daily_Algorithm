A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
my_lst = []

for index in range(2):
    if A[index] == B[index]:
        my_lst.append(C[index])
    elif A[index] == C[index]:
        my_lst.append(B[index])
    else:
        my_lst.append(A[index])
print(f'{my_lst[0]} {my_lst[1]}')