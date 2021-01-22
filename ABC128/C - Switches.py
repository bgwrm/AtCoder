n, m = (int(_) for _ in input().split())
s = [[int(_) for _ in input().split()[1:]] for i in range(m)]
p = [int(_) for _ in input().split()]
ans = 0
for i in range(2**n):
    for j in range(m):
        c = 0
        for k in s[j]:
            if (1<<(k-1))&i:
                c += 1
        if c%2 != p[j]:
            break
    else:
        ans += 1
print(ans)