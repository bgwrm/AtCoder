x = int(input())
now = 100
ans = 0

while now < x:
    now = now + now // 100
    ans += 1

print(ans)