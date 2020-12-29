s = input()
print('AC' if s[0] == 'A' and s[2:-1].count('C') == 1 and s.replace('A','').replace('C','').islower() else 'WA')