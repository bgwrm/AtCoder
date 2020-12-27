import itertools
n = int(input())
l = ['a', 'b', 'c']
c = itertools.product(l, repeat=n)

for s in c:
    print(''.join(s))