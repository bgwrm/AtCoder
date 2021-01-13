s = input()
t = input()
for i in range(len(s)):
    if s == t:
        print(i)
        exit()
    s = s[-1] + s[:-1]
print(-1)