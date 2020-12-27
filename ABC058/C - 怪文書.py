n = int(input())
s = [input() for _ in range(n)]
l = [51] * 26
ans = ''

for i in s:
    for j in range(26):
        l[j] = min(l[j], i.count(chr(97+j)))

for i in range(26):
    ans += chr(97+i) * l[i]

print(ans)