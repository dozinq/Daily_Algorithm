word = input()
total = 0

for index in word:
    if ord(index) <= 67:
        total += 3
    elif ord(index) <= 70:
        total += 4
    elif ord(index) <= 73:
        total += 5
    elif ord(index) <= 76:
        total += 6
    elif ord(index) <= 79:
        total += 7
    elif ord(index) <= 83:
        total += 8
    elif ord(index) <= 86:
        total += 9
    elif ord(index) <= 90:
        total += 10

print (total)
