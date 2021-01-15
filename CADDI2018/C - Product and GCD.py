n, p = (int(_) for _ in input().split())
l = []
ans = 1
while p%2 == 0:
    l += [2]
    p //= 2
f = 3
while f*f <= p:
    if p%f == 0:
        l += [f]
        p //= f
    else:
        f += 2
if p != 1:
    l += [p]
s = set(l)
for i in s:
    ans *= i**(l.count(i)//n)
print(ans)