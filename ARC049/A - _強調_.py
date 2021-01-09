s = input()
l = [int(_) for _ in input().split()]
print(s[:l[0]]+'"'+s[l[0]:l[1]]+'"'+s[l[1]:l[2]]+'"'+s[l[2]:l[3]]+'"'+s[l[3]:])