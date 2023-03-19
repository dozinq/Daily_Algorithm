import sys
sys.stdin = open('BOJ/input.txt')

N = int(input())

print('CY') if N % 2 == 0 else print('SK')