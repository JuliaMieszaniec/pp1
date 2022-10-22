x=int(input('Podaj pierwszą współrzędną:'))
y=int(input('Podaj pierwszą współrzędną:'))
if x>0 and y>0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
if x>0 and y<0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
if x<0 and y>0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
if x<0 and y<0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')