import datetime
s = input()
d = datetime.date(int(s[0:4]),int(s[5:7]),int(s[8:10]))
print('Heisei' if d <= datetime.date(2019,4,30) else 'TBD')