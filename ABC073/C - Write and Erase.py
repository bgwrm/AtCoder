import collections
n = int(input())
l = [input() for _ in range(n)]
c = collections.Counter(l)
ans = 0

for i in c.values():
    ans += i % 2

print(ans)