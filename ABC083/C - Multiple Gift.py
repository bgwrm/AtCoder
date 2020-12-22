x, y = (int(_) for _ in input().split())
ans = 0
while x <= y:
    x *= 2
    ans += 1
print(ans)