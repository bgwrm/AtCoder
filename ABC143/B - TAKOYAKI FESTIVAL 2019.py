n = int(input())
d = [int(_) for _ in input().split()]
total = sum(d)
ans = 0

for i in d:
    ans += i * (total - i)

print(ans//2)