import datetime
s = input()
d = datetime.date(int(s[0:4]), int(s[5:7]), int(s[8:10]))

while True:
    if d.year % (d.month * d.day) == 0:
        print(str(d).replace('-', '/'))
        exit()
    d += datetime.timedelta(days=1)