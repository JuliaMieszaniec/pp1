
wzrost=int(input('Podaj wzrost w cm: '))
cale = round(wzrost/2.54,2)
stopy = (cale//12)
reszta = cale%12
print( f'I am {wzrost} tall, i.e. {stopy} feet and {reszta} inches.')
