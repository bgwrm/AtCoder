a, b = (int(_) for _ in input().split())
p = [int(_) for _ in input().split()]
q = [int(_) for _ in input().split()]
l = ['x']*10
for i in p:
    l[i] = '.'
for i in q:
    l[i] = 'o'
print(l[7], l[8], l[9], l[0])
print(' ' + l[4], l[5], l[6])
print('  ' + l[2], l[3])
print('   ' + l[1])