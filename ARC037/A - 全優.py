n = int(input())
m = [int(_) for _ in input().split()]
ans = 0
for i in m:
    if i < 80:
        ans += 80 - i
print(ans)