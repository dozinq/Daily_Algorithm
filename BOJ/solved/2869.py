A, B, V = map(int, input().split())

# ans는 1부터 증가하면서, (ans*A)-(B*(ans-1)) >= V 일 때, ans의 값을 출력하는 것이다.
# 다만, 시간 문제가 있다. ans >= (V-B)/(A-B) 일 때의 ans값을 출력하면 된다.
ans = (V-B)/(A-B)

if ans % 1 == 0:
    print(int(ans))
else:
    print(int(ans)+1)


# 아래는 시간조절에 실패하여 고민했던 코드이다.
# if A-B == 1:
#     print(V-A+(A-B))

# ans = V//A
# V = V-(ans*(A-B))
# if V - A <= 0:
#     print(ans+1)
# else:
#     while (A-B > 1):
#         V -= A
#         if V <= 0:
#             print(ans)
#             break
#         V += B
#         ans += 1