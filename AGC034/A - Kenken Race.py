n, a, b, c, d = (int(_) for _ in input().split())
s = input()

if '##' in s[a-1:c] or '##' in s[b-1:d]:
    print('No')
    exit()
if c < d or '...' in s[b-2:d+1]:
    print('Yes')
else:
    print('No')