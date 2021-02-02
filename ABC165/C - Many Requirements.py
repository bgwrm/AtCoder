import itertools
n, m, q = (int(_) for _ in input().split())
abcd = [[int(_) for _ in input().split()] for i in range(q)]
com = itertools.combinations_with_replacement(range(1, m+1), n)
ans = 0
for co in com:
    p = 0
    for a, b, c, d in abcd:
        if co[b-1]-co[a-1] == c:
            p += d
    ans = max(p, ans)
print(ans)