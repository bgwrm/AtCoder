# 逆元？
x, y = (int(_) for _ in input().split())
ans, mod, n = 1, 10**9+7, (x+y)//3
a, b, r = x-n, y-n, min(x, y)-n
if (x+y)%3 != 0 or a < 0 or b < 0:
    print(0)
    exit()
for i in range(r):
    ans = ans*(n-i)*pow(i+1, mod-2, mod)%mod
print(ans)