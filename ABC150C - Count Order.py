import itertools

n = int(input())
p = input().replace(' ','')
q = input().replace(' ','')
nlist = list(itertools.permutations([_ for _ in range(1, n+1)]))
a = 0
b = 0

for i in range(len(nlist)):
    s = (str(nlist[i])[1:-1].replace(', ',''))
    if s == p:
        a = i + 1
    if s == q:
        b = i + 1

print(abs(a - b))