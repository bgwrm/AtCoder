from collections import Counter
s = list(input())
c = sum(i%2 for i in Counter(s).values())
print(len(s) if c == 0 else ((len(s)-c)//2)//c*2+1)