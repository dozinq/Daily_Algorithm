import sys

two_num = list(sys.stdin.readline().split())

sangsoo_1 = two_num[0][::-1]
sangsoo_2 = two_num[1][::-1]

if int(sangsoo_1) - int(sangsoo_2) >= 0:
    print(sangsoo_1)
else:
    print(sangsoo_2)