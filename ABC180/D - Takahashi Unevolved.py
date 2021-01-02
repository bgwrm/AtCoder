x, y, a, b = (int(_) for _ in input().split())
ans = 0
while a*x<=x+b and a*x<y:
    x *= a
    ans += 1
print(ans+(y-x-1)//b)