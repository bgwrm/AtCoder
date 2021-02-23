n = int(input())
a, s = ['a'], 'abcdefghij'
for i in range(n-1):
    a = [p+q for p in a for q in s[:len(set(p))+1]]
print(*a)