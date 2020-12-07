n = int(input())
a = [int(_) for _ in input().split()]
sum = sum(a)
ans = 0

for i in range(n):
    sum -= a[i]
    ans += sum * a[i]
    ans = ans % (10**9 + 7)

print(ans)