n = int(input())
a = b = ba = ab = 0
for _ in range(n):
    s = input()
    if s[-1] == 'A':
        a += 1
    if s[0] == 'B':
        b += 1
    if s[-1] == 'A' and s[0] == 'B':
        ba += 1
    ab += s.count('AB')
print(min(a, b)+ab-(a == b == ba > 0))