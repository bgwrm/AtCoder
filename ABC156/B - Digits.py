n, k = (int(_) for _ in input().split())
ans = 1

while True:
    if n < k**ans:
        print(ans)
        exit()
    ans += 1