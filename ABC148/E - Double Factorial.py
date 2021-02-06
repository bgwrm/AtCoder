n = int(input())
if n%2:
    exit(print(0))
ans = 0
while n:
    n //= 5
    ans += n//2
print(ans)