a, b = (int(_) for _ in input().split())
print(b//4-b//100+b//400-(a-1)//4+(a-1)//100-(a-1)//400)