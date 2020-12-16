s = input()
ans = 753
for i in range(len(s)-2):
    n = abs(753 - int(s[i:i+3]))
    if n < ans:
        ans = n
print(ans)