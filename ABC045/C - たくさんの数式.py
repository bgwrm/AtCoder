import itertools
s = list(input())
ans, l = 0, ['']*(2*len(s)-1)
for i in range(len(s)):
    l[2*i] = s[i]
for c in itertools.product(['+',''], repeat=len(s)-1):
    for i in range(len(c)):
        l[2*i+1] = c[i]
    ans += eval(''.join(l))
print(ans)