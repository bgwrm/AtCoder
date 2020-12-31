n, a, b = (int(_) for _ in input().split())
p = 0

for i in range(n):
    s, d = (input().split())
    if s == 'East':
        p += a if int(d) < a else b if b < int(d) else int(d)
    else:
        p -= a if int(d) < a else b if b < int(d) else int(d)

if p < 0:
    print('West '+str(abs(p)))
elif p == 0:
    print(0)
else:
    print('East '+str(p))