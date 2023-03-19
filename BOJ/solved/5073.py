import sys
sys.stdin = open('BOJ/input.txt')

while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data == [0, 0, 0]:
        break
    data.sort(reverse=True)
    if data[0] >= data[1] + data[2]:
        print('Invalid')
    elif data[0] == data[1] == data[2]:
        print('Equilateral')
    elif data[0] == data[1] or data[1] == data[2] or data[0] == data[2]:
        print('Isosceles')
    else:
        print('Scalene')
