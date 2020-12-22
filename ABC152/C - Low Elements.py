n = int(input())
p = [int(_) for _ in input().split()]
num = p[0]
ans = 0

for i in p:
    if i <= num:
        num = i
        ans += 1

print(ans)