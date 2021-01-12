n = int(input())
ans = 10**12
for i in range(1,n//2+1):
    p = sum(int(_) for _ in str(i)) + sum(int(_) for _ in str(n-i))
    ans = min(p, ans)
print(ans)