money=int(input('Podaj ilość w zł: '))
x=money//5
y=money%5
z=y//2
g=y%2
print(f'{money} zł w monetach to:')
print(f'5zł:{x}')
print(f'2zł:{z}')
print(f'1zł:{g}')