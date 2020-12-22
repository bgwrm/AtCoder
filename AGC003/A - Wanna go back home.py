s = input()
if (s.count('N') >= 1 and s.count('S') == 0) or (s.count('S') >= 1 and s.count('N') == 0) or (s.count('W') >= 1 and s.count('E') == 0) or (s.count('E') >= 1 and s.count('W') == 0):
    print('No')
else:
    print('Yes')