s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)

for i in range(min(len(s), len(t))):
    if s[i] < t[i]:
        print('Yes')
        exit()
    elif s[i] > t[i]:
        print('No')
        exit()

if len(s) < len(t):
    print('Yes')
    exit()
else:
    print('No')
    exit()