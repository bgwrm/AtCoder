l, x, y, s, d = (int(_) for _ in input().split())
r = abs(d-s)
ans = []
if s == d:
    ans += [0]
elif s < d:
    if x < y:
        ans += [(l-r)/(y-x)]
    ans += [r/(x+y)]
else:
    if x < y:
        ans += [r/(y-x)]
    ans += [(l-r)/(x+y)]
print(min(ans))