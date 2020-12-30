s = input()
c1, c2 = 0, 0

if len(s) == 1:
    print(0)
    exit()

for i in range(0, len(s), 2):
    if s[i] == '0':
        c1 += 1
    else:
        c2 += 1

for i in range(1, len(s), 2):
    if s[i] == '0':
        c2 += 1
    else:
        c1 += 1

print(min(c1, c2))