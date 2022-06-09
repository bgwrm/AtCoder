n, p, q = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        p1 = a[i]*a[j]%p
        for k in range(j+1, n):
            p2 = p1*a[k]%p
            for l in range(k+1, n):
                p3 = p2*a[l]%p
                for m in range(l+1, n):
                    if (p3*a[m])%p == q:
                        ans += 1
print(ans)