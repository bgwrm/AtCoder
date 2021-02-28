n = int(input())
s = set()
for i in range(2, int(n**0.5)+1):
    j = 2
    while i**j <= n:
        s.add(i**j)
        j += 1
print(n-len(set(s)))