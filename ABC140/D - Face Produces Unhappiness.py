n, k = (int(_) for _ in input().split())
s = input()
c = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        c += 1
print(min(n-1, c+2*k))