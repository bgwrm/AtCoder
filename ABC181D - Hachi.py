from collections import Counter

s = input()
cs = Counter(s)

if len(s) <= 2:
    if int(''.join(s)) % 8 == 0 or int(''.join(s[::-1])) % 8 == 0:
        print('Yes')
        exit()
    else:
        print('No')
        exit()

for i in range(112, 1000, 8):
    if not Counter(str(i)) - cs:
        print('Yes')
        exit()

print('No')