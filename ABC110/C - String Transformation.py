from collections import Counter
s = Counter(input()).values()
t = Counter(input()).values()
print('Yes' if Counter(s) == Counter(t) else 'No')