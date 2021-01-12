s = input()
for i in range(len(s)):
    if s[i] == 'C' and s[i+1:].count('F') > 0:
        print('Yes')
        exit()
print('No')