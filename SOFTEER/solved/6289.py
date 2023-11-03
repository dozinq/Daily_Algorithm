import sys

# def find(x):
#   if parents[x] != x:
#     return find(parents[x])
#   return x

# def union(x, y):
#   x, y = find(x), find(y)
#   if x < y:
#     parents[y] = x
#   elif x > y:
#     parents[x] = y
#   return    

N, M = map(int, input().split())
data = list(map(int, input().split()))

# parents = list(i for i in range(N))
friends = [list() for _ in range(N)]
for _ in range(M):
  a, b = map(lambda x: int(x)-1, input().split())
  friends[a].append(b)
  friends[b].append(a)
  # union(a, b)

ans = 0
for i in range(N):
  tmp_flag = 1
  for j in range(len(friends[i])):
    if data[friends[i][j]] >= data[i]:
      tmp_flag = 0
      break
  if tmp_flag == 1:
    ans += 1

print(ans)
  
  
# best_dict = {}
# for i in range(N):
#   if best_dict.get(find(i)):
#     print(best_dict.get(find(i)))
#     best_dict[find(i)] = max(best_dict.get(find(i)), data[i])
#   else:
#     best_dict[find(i)] = data[i]

# print(best_dict)