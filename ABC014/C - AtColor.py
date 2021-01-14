n = int(input())
c = ans = 0
l = [0] * 1000002
for i in range(n):
    a, b = (int(_) for _ in input().split())
    l[a] += 1
    l[b+1] -= 1
for i in l:
    c += i
    ans = max(c, ans)
print(ans)