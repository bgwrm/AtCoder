n = int(input())
sp = [input().split() for _ in range(n)]
s = [sp[i][0] for i in range(n)]
p = [int(sp[i][1]) for i in range(n)]

if max(p) * 2 > sum(p):
    print(s[p.index(max(p))])
else:
    print('atcoder')