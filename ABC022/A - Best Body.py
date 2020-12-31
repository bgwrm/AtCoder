n, s, t = (int(_) for _ in input().split())
w = int(input())
a = [int(input()) for _ in range(n-1)]
ans = 1 if s <= w and w <= t else 0

for i in a:
    w += i
    if s <= w and w <= t:
        ans += 1

print(ans)