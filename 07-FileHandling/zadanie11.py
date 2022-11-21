a=['Shrek','Harry Potter', 'Incepcja','Duma i uprzedzenie','Pokuta']

f=open('films.txt','w', encoding='utf-8')

for x in a:
    f.write(f'{x}\n')

f.close()
