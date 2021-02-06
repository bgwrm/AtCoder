n = int(input())
s = list(input())
ans = 0
for i in range(1000):
    c, p = 0, str(i).zfill(3)
    for j in s:
        if j == p[c]:
            c += 1
            if c == 3:
                ans += 1
                break
print(ans)