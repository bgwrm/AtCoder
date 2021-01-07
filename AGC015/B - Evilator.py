s = input()
ans = len(s)*(len(s)-1)

for i in range(1,len(s)-1):
    if s[i] == 'U':
        ans += i
    else:
        ans += len(s)-i-1
print(ans)