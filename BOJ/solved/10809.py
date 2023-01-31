S = input()
alphabet_lst = []
for i in range(97, 123):
    alphabet_lst.append(chr(i))

for index in alphabet_lst:
    print(S.find(index), end=' ')