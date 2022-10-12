a=float(input('Podaj długośc pierwszego boku trojkąta:'))
b=float(input('Podaj długośc drugiego boku trojkąta:'))
c=float(input('Podaj długośc trzeciego boku trojkąta:'))
p=(a+b+c)/2
pole=p*(p-a)*(p-b)*(p-c)
pole=pole**(0.5)
print('Pole trójkąta wynosi: ' , pole )