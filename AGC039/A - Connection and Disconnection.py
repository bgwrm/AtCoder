s = list(input())
k = int(input())
c0, c1, c2, n = 1, 0, 0, len(s)
l = []
for i in range(n):
    if i < n-1 and s[i] == s[i+1]:
        c0 += 1
    else:
        l += [c0]
        c1 += c0//2
        c0 = 1
if s[0] == s[-1] and l[0]%2 == l[-1]%2 == 1:
    c2 = k-1
print(n*k//2 if len(set(s)) == 1 else k*c1+c2)