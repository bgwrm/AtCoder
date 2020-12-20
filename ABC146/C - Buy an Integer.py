a, b, x = (int(_) for _ in input().split())
n = 0

if a + b > x:
    print(0)
    exit()

for i in range(9, -1, -1):
    if a * (10**i) + (i + 1) * b <= x:
        n = i
        break

ans = min((x - (n + 1) * b) // a, 10**(n+1)-1)
print(10**9 if ans >= 10**9 else ans)