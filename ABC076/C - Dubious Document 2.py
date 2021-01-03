s = input()
t = input()
l = []

for i in range(len(s)-len(t)+1):
    for j in range(len(t)):
        if s[i+j] != '?' and s[i+j] != t[j]:
            break
    else:
        l += [(s[:i] + t + s[i+len(t):]).replace('?','a')]

print('UNRESTORABLE' if len(l) == 0 else min(l))