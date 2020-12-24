n = int(input())
s = list(input())
ans = ''
for a in s:
    if ord(a)+n > ord('Z'):
        ans += chr(ord(a)+n-26)
    else:
        ans += chr(ord(a)+n)

print(ans)