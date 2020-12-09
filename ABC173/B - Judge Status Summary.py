import sys
input = sys.stdin.readline

n = int(input())
s = [input().strip() for i in range(n)]

print('AC x ' + str(s.count('AC')))
print('WA x ' + str(s.count('WA')))
print('TLE x ' + str(s.count('TLE')))
print('RE x ' + str(s.count('RE')))