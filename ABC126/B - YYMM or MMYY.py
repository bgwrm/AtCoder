s = input()
if int(s[:2]) > 0 and int(s[:2]) <= 12 and int(s[2:]) > 0 and int(s[2:]) <= 12:
    print('AMBIGUOUS')
elif (int(s[:2]) > 12 or int(s[:2]) == 0) and int(s[2:]) > 0 and int(s[2:]) <= 12:
    print('YYMM')
elif (int(s[2:]) > 12 or int(s[2:]) == 0) and int(s[:2]) > 0 and int(s[:2]) <= 12:
    print('MMYY')
else:
    print('NA')