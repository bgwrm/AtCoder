a, b = (int(_) for _ in input().split())
s = input()
print('Yes' if str.isnumeric(s[:a]) and s[a] == '-' and str.isnumeric(s[a+1:]) and len(s) == a + b + 1 else 'No')