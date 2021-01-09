n = int(input())
ans = 0
for i in range(n):
    a, b = (int(_) for _ in input().split())
    ans += a*b
print(int(ans*1.05))