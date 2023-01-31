a = int(input())
b = int(input())

print('%d' % (a*(b%10)))
print('%d' % (a*((b%100)//10)))
print('%d' % (a*(b//100)))
print('%d' % (a*b))