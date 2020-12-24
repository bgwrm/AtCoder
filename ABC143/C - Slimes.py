n = int(input())
s = input()
left = s[0]
ans = 1

for i in range(1, n):
    if left != s[i]:
        left = s[i]
        ans += 1

print(ans)