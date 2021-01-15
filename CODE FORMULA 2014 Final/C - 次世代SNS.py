import re
s = input()
ans = sorted(set(re.findall('@(\w+)', s)))
print(*ans, sep='\n')