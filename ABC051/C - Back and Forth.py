sx, sy, tx, ty = (int(_) for _ in input().split())
dx, dy = tx-sx, ty-sy
print('U'*dy+'R'*dx+'D'*dy+'L'*(dx+1)+'U'*(dy+1)+'R'*(dx+1)+'DR'+'D'*(dy+1)+'L'*(dx+1)+'U')