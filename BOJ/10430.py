A, B, C = map(int, input().split())

print('%d' % ((A+B)%C))
print('%d' % (((A%C)+(B%C))%C))
print('%d' % ((A*B)%C))
print('%d' % (((A%C)*(B%C))%C))