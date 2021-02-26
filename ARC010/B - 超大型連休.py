n = int(input())
md = sorted([[int(_) for _ in input().split('/')] for i in range(n)])
ans, c, p, q = 2, 0, [0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335], [0]*500
for i in range(1, 367):
    if i%7 in [0, 1]:
        q[i] = 1
for m, d in md:
    i = 0
    while True:
        if q[p[m]+d+i] == 0:
            q[p[m]+d+i] = 1
            break
        else:
            i += 1
for i in range(1, 367):
    if q[i] == 1:
        c += 1
    else:
        ans = max(c, ans)
        c = 0
print(max(c, ans))