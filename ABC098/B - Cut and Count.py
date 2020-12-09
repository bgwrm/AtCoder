n = int ( input ())
s = input ()
alphabet = [ chr ( ord ( "a" )+i) for i in range ( 26 )]
ans = 0
for i in range (n- 1 ):
    x = s[:i+1]
    y = s[i+1:]
    count = 0
    for a in alphabet:
        if x.count(a) > 0 and y.count(a) > 0:
            count += 1
    if count > ans:
        ans = count
print (ans)