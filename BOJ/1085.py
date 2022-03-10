# from math import *
#
# x, y, w, h = map(int, input().split())
# row = col = 0
#
# if x >= (w//2):
#     if y >= (h//2):
#         row = w-x
#         col = h-y
#     else:
#         row = w-x
#         col = y
# else:
#     if y >= h//2:
#         row = x
#         col = h-y
#     else:
#         row = x
#         col = y
#
# ans = (sqrt((row**2)+(col**2)))
# print(ans)

x, y, w, h = map(int, input().split())

ans = min(x, y, w-x, h-y)

print(ans)