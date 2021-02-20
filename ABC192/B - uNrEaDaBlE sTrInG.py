s = input()
s1, s2 = ''.join(s[::2]), ''.join(s[1::2])
print('Yes' if s1.islower() and (s2.isupper() or s2=='') else 'No')