n = int(input())
ans = 0
if n >= 10**3:
    ans += min(10**6-1, n)-10**3+1
if n >= 10**6:
    ans += 2*(min(10**9-1, n)-10**6+1)
if n >= 10**9:
    ans += 3*(min(10**12-1, n)-10**9+1)
if n >= 10**12:
    ans += 4*(min(10**15-1, n)-10**12+1)
if n == 10**15:
    ans += 5
print(ans)