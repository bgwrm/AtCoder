n = int(input())
a = [int(_) for _ in input().split()]
ans = 0
for i in a:
    count = 0
    while (i-count)%2 == 0 or (i-count)%3 == 2:
        count += 1
    ans += count
print(ans)