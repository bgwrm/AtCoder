n, m = (int(_) for _ in input().split())
x, y = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
ans = t = i = j = 0
while True:
    while True:
        if t <= a[i]:
            t = a[i]+x
            break
        else:
            i += 1
            if i == n:
                print(ans)
                exit()
    while True:
        if t <= b[j]:
            t = b[j]+y
            ans += 1
            break
        else:
            j += 1
            if j == m:
                print(ans)
                exit()
print(ans)