x = input()
print('YES' if len(x.replace('ch','').replace('o','').replace('k','').replace('u','')) == 0 else 'NO')