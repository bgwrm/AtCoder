n = int(input())
t = [int(input()) for _ in range(n)]
sum_t = sum(t)
ans = 10**3
for i in range(2**n):
    x = 0
    for j in range(n):
        if (i>>j)&1:
            x += t[j]
    ans = min(max(x, sum_t-x), ans)
print(ans)