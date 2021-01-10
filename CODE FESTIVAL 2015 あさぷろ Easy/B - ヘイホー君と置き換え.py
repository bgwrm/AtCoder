n = int(input())
s = input()
ans = 0
if n%2 == 1:
    print(-1)
    exit()
for i in range(n//2):
    if s[i] != s[i+n//2]:
        ans += 1
print(ans)