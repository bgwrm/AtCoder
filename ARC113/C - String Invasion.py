s = list(input())
ans, i, l, n = 0, len(s)-1, [0]*26, len(s)
while i > 0:
    index = ord(s[i])-ord('a')
    if s[i] == s[i-1]:
        ans += n-i-1-l[index]
        l = [0]*26
        l[index] = n-i+1
        i -= 2
    else:
        l[index] += 1
        i -= 1
print(ans)