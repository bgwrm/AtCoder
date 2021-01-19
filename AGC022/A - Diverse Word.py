s = input()
l = 'zyxwvutsrqponmlkjihgfedcba'
if s == l:
    print(-1)
elif len(s) != 26:
    print(s+min(set(l)-set(s)))
else:
    for i in range(24, -1, -1):
        for j in range(25, i, -1):
            if s[i] < s[j]:
                print(s[:i]+s[j])
                exit()