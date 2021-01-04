s = input()
k = 'keyence'

for i in range(len(s)):
    for j in range(i, len(s)):
        if k == s[:i] + s[j:]:
            print('YES')
            exit()

print('NO')