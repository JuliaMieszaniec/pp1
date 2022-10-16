import random
a=random.randint(1, 6)
b=int(input('Podaj cyfrę od 1 do 6: '))
row=a==b
print(f'Kompter wylosował {a}, więc to jest {row}')