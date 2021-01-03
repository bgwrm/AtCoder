h, w, k = (int(_) for _ in input().split())
c = [input() for _ in range(h)]
ans = 0
for i in range(2**h):
    for j in range(2**w):
        b = 0
        for x in range(h):
            for y in range(w):
                if (i>>x)&1 and (j>>y)&1 and c[x][y] == '#':
                    b += 1
        if b == k:
            ans += 1
print(ans)