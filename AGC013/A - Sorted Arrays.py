n = int(input())
a = [int(_) for _ in input().split()]
now, inc, ans = a[0], 0, 1

for i in range(1, n):
    if now < a[i]:
        if inc == 0:
            inc = 1
        elif inc == -1:
            ans += 1
            inc = 0
    if now > a[i]:
        if inc == 1:
            ans += 1
            inc = 0
        elif inc == 0:
            inc = -1
    now = a[i]

print(ans)