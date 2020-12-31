n = int(input())
d, x = (int(_) for _ in input().split())
a = [int(input()) for _ in range(n)]
ans = x
for i in a:
    ans += (d-1)//i + 1
print(ans)