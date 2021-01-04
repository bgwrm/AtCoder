n = int(input())
s = input()
t = input()
for i in range(n,-1,-1):
    if s[n-i:] == t[:i]:
        print(2*n-i)
        break