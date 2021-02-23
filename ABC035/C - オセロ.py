n, q = (int(_) for _ in input().split())
t = [0]*(n+2)
for _ in range(q):
    l, r = (int(_) for _ in input().split())
    t[l] += 1
    t[r+1] -= 1
for i in range(1, n+1):
    t[i] = (t[i-1]+t[i])%2
print(''.join(map(str, t[1:n+1])))