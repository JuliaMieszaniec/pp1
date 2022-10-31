suma=0
x=0
while True:
    a=int(input('Podaj liczbę:'))
    if a==0:
        break
    else:
        suma= suma + a
        x= x +1

srednia=suma/x
print(f'RESULT: Quantity={x}, Sum={suma}, Mean={srednia}')