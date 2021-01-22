s = input()
n = len(s)
l = [1]*n
for i in range(n):
    if s[i] == 'R' and s[i+1] == 'R':
        l[i+2] += l[i]
        l[i] = 0
for i in reversed(range(n)):
    if s[i] == 'L' and s[i-1] == 'L':
        l[i-2] += l[i]
        l[i] = 0
print(*l)