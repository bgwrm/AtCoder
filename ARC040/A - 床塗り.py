n = int(input())
s = [input() for _ in range(n)]
t, a = 0, 0
for i in s:
    t += i.count('R')
    a += i.count('B')
print('TAKAHASHI' if t>a else 'AOKI' if t<a else 'DRAW')