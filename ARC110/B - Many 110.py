n = int(input())
t = input()
if t.count('111') + t.count('00') + t.count('010')> 0:
    print(0)
elif t == '1':
    print(2*10**10)
elif t == '0' or t == '11' or t =='10' or t == '110':
    print(10**10)
elif t == '01':
    print(10**10-1)
elif t[:3] != '110' and t[:-3] != '110':
    print(10**10-(n-2)//3-1)
elif t[:3] != '110' or t[:-3] != '110':
    print(10**10-(n-1)//3)
else:
    print(10**10-n//3)