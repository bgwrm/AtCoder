n, k = (int(_) for _ in input().split())
s = list(input())

if s[k-1] == 'A':
    s[k+-1] = 'a'
elif s[k-1] == 'B':
    s[k-1] = 'b'
elif s[k-1] == 'C':
    s[k-1] = 'c'

print(''.join(s))