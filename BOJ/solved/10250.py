T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    room_num = 0

    if (N % H) == 0:
        floor = H * 100
        room_num = (N // H)
        print(floor + room_num)
    else:
        floor = (N % H) * 100
        room_num = (N // H) + 1
        print(floor + room_num)


    # ans = []

    # if N % H == 0:
    #     ans.append(H)
    # else:
    #     ans.append(N % H)
    
    # if N % H == 0:
    #     if N // H < 10:
    #         ans.append(0)
    #         ans.append(N // H)
    #     else:
    #         ans.append(N // H)
    # else:
    #     if N // H < 10:
    #         ans.append(0)
    #         ans.append((N // H)+1)
    #     else:
    #         ans.append((N // H)+1)

    # for index in ans:
    #     print(index, end = "")
    # print()


# for i in range(T):

#     H, W, N = map(int, input().split())

#     ans=[]

#     if (N % H) == 0:
#         ans.append(H)
#     else:
#         ans.append(N % H)

#     if (N % H == 0):
#         ans.append(0)
#         ans.append((N // H))
#     elif (N // H) + 1 < 10:
#         ans.append(0)
#         ans.append((N // H) + 1)
#     else:
#         ans.append((N // H) + 1)

#     for index in ans:
#         print(index, end = "")
#     print()

