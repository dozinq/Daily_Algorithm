N = input()
num = 0

if int(N) < 10:
    N0 = 0
    N1 = int(N)
else:
    N0 = int(N[0])
    N1 = int(N[1])

N_true_0 = N0
N_true_1 = N1

while(1):
    num += 1
    N_new = N0 + N1
    if N_new >= 10:
        N_new -= 10
    N0 = N1
    if N1 == N_true_0 and N_new == N_true_1:
        break
    N1 = N_new

print(num)