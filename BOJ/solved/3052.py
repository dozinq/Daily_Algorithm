my_lst = list()

for i in range(10):
    my_lst.append((int(input())%42))

print(len(set(my_lst)))
