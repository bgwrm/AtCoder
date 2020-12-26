n, x = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
f = '0' + str(n) + 'b'
s = format(x, f)[::-1]
ans = 0

for i in range(n):
    if s[i] == '1':
        ans += a[i]

print(ans)