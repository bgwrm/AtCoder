s = input()
print(len(s) - s.index('A') - s[::-1].index('Z'))