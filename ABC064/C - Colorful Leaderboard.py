n = int(input())
a = [int(_) for _ in input().split()]
l = [0] * 9
ans = 0

for i in a:
    l[min(i//400, 8)] += 1

for i in range(8):
    if l[i] > 0:
        ans += 1

print(max(ans, 1), ans+l[8])