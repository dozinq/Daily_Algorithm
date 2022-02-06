N = int(input())
min_room = 1
i = 1

while(True):
    if(N<=i):
        print(min_room)
        break
    i += (6*min_room)
    min_room += 1