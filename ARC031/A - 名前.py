s = input()
for i in range(len(s)//2+1):
    if s[i] != s[-1*(i+1)]:
        print('NO')
        exit()
print('YES')