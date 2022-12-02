a=[15, 8, 31, 47, 2, 19]

liczby=len(a)
suma=0

i=0
while i<len(a):
    suma+=a[i]
    i+=1

print(suma)
srednia=suma/liczby
print(srednia)