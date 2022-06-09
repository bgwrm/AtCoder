from collections import defaultdict
n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
d = defaultdict(int)
ans = j = 0
for i in range(n):
    d[a[i]] += 1
    while len(d) > k:
        d[a[j]] -= 1
        if d[a[j]] == 0: del(d[a[j]])
        j += 1
    ans = max(ans, i-j+1)
print(ans)