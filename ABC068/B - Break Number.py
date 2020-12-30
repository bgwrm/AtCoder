n = int(input())
i = 1
ans = 1
while 2 ** i <= n:
    ans = 2 ** i
    i += 1
print(ans)