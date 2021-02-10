n = int(input())
w = input().split()
l = ['z','b','d','t','f','l','s','p','h','n','r','c','w','j','q','v','x','m','k','g']
ans = []
for s in w:
    k = ''
    for c in list(s):
        c = c.lower()
        if c in l:
            k += str(l.index(c)%10)
    if len(k) > 0:
        ans += [k]
print(*ans)