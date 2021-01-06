r, g, b, n = (int(_) for _ in input().split())
ans = 0
for i in range(n//r+1):
    for j in range((n-i)//g+1):
        num = n-r*i-g*j
        if num%b == 0 and num >= 0:
            ans += 1
print(ans)