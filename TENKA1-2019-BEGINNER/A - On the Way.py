a, b, c = (int(_) for _ in input().split())
print('Yes' if a<c<b or a>c>b else 'No')