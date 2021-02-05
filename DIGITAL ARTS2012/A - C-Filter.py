import re
s = input().split()
n = int(input())
for i in range(n):
    ng = re.compile(input().replace('*', '.'))
    for i in range(len(s)):
        if ng.fullmatch(s[i]):
            s[i] = '*'*len(s[i])
print(*s)