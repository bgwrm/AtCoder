n = int(input())
if n%2 == 1:
    print(0)
else:
    ans = 0
    while n//5 > 0:
        n //= 5
        ans += n//2
    print(ans)