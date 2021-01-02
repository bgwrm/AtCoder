a, b = (input().split())
va, vb = 0, 0

for i in a:
    va += int(i)
for i in b:
    vb += int(i)

print(max(va, vb))