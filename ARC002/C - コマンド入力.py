import itertools
n = int(input())
c = input()
ans, p = n, list('ABXY')
for l in itertools.product(p, repeat=2):
    co = c
    for r in itertools.product(p, repeat=2):
        ans = min(len(co.replace(''.join(l),'L').replace(''.join(r),'R')), ans)
print(ans)