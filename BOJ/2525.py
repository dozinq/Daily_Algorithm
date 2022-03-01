A, B = map(int, input().split())
minute = int(input())
A += minute//60
B += minute%60

if B >= 60:
    A += B//60
    B %= 60
if A >= 24:
    A %= 24

print(A, B)