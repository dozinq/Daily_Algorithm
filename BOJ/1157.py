import sys

word = sys.stdin.readline()
ans_lst = list(range(65, 91))
my_dict = {}
total = 0

for index in ans_lst:
    a = word.count(chr(index)) + word.count(chr(index + 32))
    # b = word.count(chr(index + 32))
    if total < a:
        total = a
        ans = chr(index)
    elif total == a:
        ans = '?'

print(ans)


# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90