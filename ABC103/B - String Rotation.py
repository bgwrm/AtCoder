s = input()
t = input()

for i in range(len(s)):
    t = t[-1] + t[:-1]
    if s == t:
        print('Yes')
        exit()
print('No')