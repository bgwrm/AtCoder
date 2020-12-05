n = int(input())
c = input()
red = c.count('R')
print((c[:red].count('W') + c[red:].count('R'))//2)