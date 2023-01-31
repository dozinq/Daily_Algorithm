data = list(map(int, input().split()))

if len(set(data)) == 1:
    ans = 10000 + data[0]*1000
elif len(set(data)) == 2:
    if data.count(data[0]) == 1:
        ans = 1000 + data[1]*100
    else:
        ans = 1000 + data[0]*100
else:
    ans = max(data)*100

print(ans)