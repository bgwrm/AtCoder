n = int(input())
l = []
if n%2 == 0:
    for i in range(2**n):
        s = r = bin(i)[2:].zfill(n)
        if s.count('1') != n//2: continue
        for _ in range(10): r = r.replace('01', '')
        if len(r) == 0: l += [s.replace('0', '(').replace('1', ')')]
print(*l, sep='\n')