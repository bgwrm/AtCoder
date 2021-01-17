n = int(input())
s = input()
ans, mod = 1, 10**9+7
for i in set(s):
    ans *= s.count(i)+1
    ans %= mod
print(ans-1)