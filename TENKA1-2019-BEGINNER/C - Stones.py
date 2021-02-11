n = int(input())
s = input()
w = ans = s.count('.')
b = 0
for i in range(n):
    if s[i] == '.':
        w -= 1
    else:
        b += 1
    ans = min(w+b, ans)
print(ans)