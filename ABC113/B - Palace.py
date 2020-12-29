n = int(input())
t, a = (int(_) for _ in input().split())
h = [int(_) for _ in input().split()]
diff = 10**6
ans = 0

for i in range(n):
    temp = t - h[i] * 0.006
    if abs(temp-a) < diff:
        diff = abs(temp-a)
        ans = i+1

print(ans)