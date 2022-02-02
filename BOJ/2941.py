word = input()

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

ans = len(word)
index = 0

while index <= len(word):
    if index+2 <= len(word)-1 and ((word[index] + word[index+1] + word[index+2]) in alphabets):
        ans -= 2
        index += 3
    elif index+1 <= len(word)-1 and ((word[index] + word[index+1]) in alphabets):
        ans -= 1
        index += 2
    else:
        index += 1

print(ans)